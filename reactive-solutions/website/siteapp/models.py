from django.db import models
from django.urls import reverse
from django.template import defaultfilters
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import uuid
import os
from tinymce.models import HTMLField
from colorful.fields import RGBColorField


# Create your models here.


# OPTIMIZE: it should to use only one function to upload files

def upload_image_slider(instance, filename):
    file_name = str(instance.slide_image).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.slide_image = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.slide_image))

def upload_image_project(instance, filename):
    file_name = str(instance.project_thumbnail).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.project_thumbnail = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.project_thumbnail))

def upload_image_service(instance, filename):
    file_name = str(instance.service_thumbnail).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.service_thumbnail = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.service_thumbnail))

def upload_icon_service(instance, filename):
    file_name = str(instance.service_icon).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.service_icon = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.service_icon))

def upload_image_post(instance, filename):
    file_name = str(instance.post_thumbnail).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.post_thumbnail = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.post_thumbnail))

def upload_image_banner(instance, filename):
    file_name = str(instance.banner_thumbnail).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.banner_thumbnail = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.banner_thumbnail))

def upload_image_page(instance, filename):
    file_name = str(instance.page_thumbnail).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.page_thumbnail = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.page_thumbnail))


def get_template_list():
    settings_dir = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
    path = '{0}/templates/page-template/'.format(str(settings_dir))
    list = os.listdir(path)
    choices = [ ('page-template/{0}'.format(template), template.split('.')[0]) for template in list ]
    return choices



class HomeSlider(models.Model):
    slide_title = models.CharField(max_length=60, help_text='Enter the title')
    slide_content = models.TextField(max_length=150, help_text='Enter the descrition')
    slide_image = models.ImageField(upload_to=upload_image_slider, default='no-img.jpg')


    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return '{0}'.format(self.slide_title)


class Banner(models.Model):
    banner_name = models.CharField(max_length=100, primary_key=True, help_text='Enter unique banner name')
    banner_title = models.CharField(max_length=500, help_text='Enter the title for banner')
    banner_content = HTMLField()
    banner_thumbnail = models.ImageField(upload_to=upload_image_banner, default='no-img.png')
    banner_button_name = models.CharField(max_length=100, help_text='Enter the button name')
    banner_button_url = models.CharField(max_length=500, help_text='Enter the button URL')


    def admin_display_banner_content(self):
        return '{0}: {1}'.format(self.banner_title, self.banner_content)

    def __str__(self):
        return '{0}'.format(self.banner_name)


class ArchiveProject(models.Model):
    id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=150, help_text='Enter the project title')
    project_content = HTMLField()
    project_thumbnail = models.ImageField(upload_to=upload_image_project, default='no-img.png')
    project_slug = models.SlugField(max_length=200, null=True)


    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'slug': self.project_slug})

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return '{0}'.format(self.project_title)


class ArchiveService(models.Model):
    id = models.AutoField(primary_key=True)
    service_title = models.CharField(max_length=200, help_text='Enter the service title')
    service_content = HTMLField()
    service_thumbnail = models.ImageField(upload_to=upload_image_service, default='no-img.png')
    service_icon = models.ImageField(upload_to=upload_icon_service, default='no-img.png')
    service_slug = models.SlugField(max_length=200, null=True)
    service_background_color = RGBColorField(default='#FFFFFF')


    def admin_display_service_slug(self):
        return '{0}'.format(self.service_slug)

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.service_slug})

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return '{0}'.format(self.service_title)


class ArchivePost(models.Model):
    id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=500, help_text='Enter the post title')
    post_content = HTMLField()
    post_thumbnail = models.ImageField(upload_to=upload_image_post, default='no-img.png')
    post_date = models.DateTimeField(auto_now_add=True)
    post_slug = models.SlugField(max_length=200, null=True)


    def admin_display_post_slug(self):
        return '{0}'.format(self.post_slug)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.post_slug})

    def __str__(self):
        return '{0}'.format(self.post_title)


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    page_title = models.CharField(unique=True, max_length=500, help_text='Enter the page title', null=False)
    page_content = HTMLField()
    page_thumbnail = models.ImageField(upload_to=upload_image_page, default='no-img.png')
    page_date = models.DateTimeField(auto_now_add=True)
    page_slug = models.SlugField(max_length=200, null=True)
    page_template = models.CharField(max_length=1000, choices=get_template_list(), default='default.html', help_text='Page template')


    def admin_display_page_slug(self):
        return '{0}'.format(self.page_slug)

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'slug': self.post_slug})

    def __str__(self):
        return '{0}'.format(self.page_title)


class SiteOption(models.Model):
    site_option_name = models.CharField(max_length=100, primary_key=True, help_text='Enter unique option name')
    site_option_value = models.TextField(max_length=1000, help_text='Enter the value for the option')


    def admin_display_site_option_value(self):
        return '{0}'.format(self.site_option_value)

    def __str__(self):
        return '{0}'.format(self.site_option_name)


class Prospect(models.Model):
    prospect_name = models.CharField(max_length=200)
    prospect_last_name = models.CharField(max_length=200)
    prospect_email = models.CharField(max_length=200)
    prospect_phone = models.CharField(max_length=15)
    prospect_website = models.CharField(max_length=200)
    prospect_message = models.TextField(max_length=5000)


    def __str__(self):
        return '{0} - {1}'.format(self.prospect_name, self.prospect_email, self.prospect_phone)


@receiver(post_save, sender=HomeSlider)
def home_slider_post_save(sender, instance, created, **kwargs):
    if created:
        instance.slide_image = str(instance.slide_image).replace('siteapp', '')
        instance.save()
    else:
        if "siteapp" in str(instance.slide_image):
            instance.slide_image = str(instance.slide_image).replace('siteapp', '')
            instance.save()


@receiver(post_save, sender=ArchiveProject)
def archive_project_post_save(sender, instance, created, **kwargs):
    if created:
        slug = defaultfilters.slugify('{0}-{1}'.format(instance.project_title[:180], instance.id))
        instance.project_slug = '{0}'.format(slug)
        instance.project_thumbnail = str(instance.project_thumbnail).replace('siteapp', '')
        instance.save()
    else:
        if "siteapp" in str(instance.project_thumbnail):
            instance.project_thumbnail = str(instance.project_thumbnail).replace('siteapp', '')
            instance.save()


@receiver(post_save, sender=ArchiveService)
def archive_service_post_save(sender, instance, created, **kwargs):
    if created:
        instance.service_slug = defaultfilters.slugify('{0}-{1}'.format(instance.service_title[:180], instance.id))
        instance.service_icon = str(instance.service_icon).replace('siteapp', '')
        instance.service_thumbnail = str(instance.service_thumbnail).replace('siteapp', '')
        instance.save()
    else:
        object_old = ArchiveService.objects.get(pk=instance.pk)
        is_diff = False
        if "siteapp" in str(instance.service_icon):
            instance.service_icon = str(instance.service_icon).replace('siteapp', '')
            is_diff = True
        if "siteapp" in str(instance.service_thumbnail):
            instance.service_thumbnail = str(instance.service_thumbnail).replace('siteapp', '')
            is_diff = True
        if is_diff:
            instance.save()


@receiver(post_save, sender=ArchivePost)
def archive_post_post_save(sender, instance, created, **kwargs):
    if created:
        instance.post_slug = defaultfilters.slugify('{0}-{1}'.format(instance.post_title[:180], instance.id))
        instance.post_thumbnail = str(instance.post_thumbnail).replace('siteapp', '')
        instance.save()
    else:
        if "siteapp" in str(instance.post_thumbnail):
            instance.post_thumbnail = str(instance.post_thumbnail).replace('siteapp', '')
            instance.save()


@receiver(post_save, sender=Page)
def page_post_save(sender, instance, created, **kwargs):
    if created:
        instance.page_slug = defaultfilters.slugify('{0}'.format(instance.page_title[:180]))
        instance.page_thumbnail = str(instance.page_thumbnail).replace('siteapp', '')
        instance.save()
    else:
        if "siteapp" in str(instance.page_thumbnail):
            instance.page_thumbnail = str(instance.page_thumbnail).replace('siteapp', '')
            instance.save()
