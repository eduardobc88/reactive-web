from django.db import models
from django.urls import reverse
from django.template import defaultfilters
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
import os
from tinymce.models import HTMLField


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


    def admin_display_service_slug(self):
        return '{0}'.format(self.service_slug)

    def get_absolute_url(self):
        return reverse('services', kwargs={'slug': self.service_slug})

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
        return reverse('blog-detail', wargs={'slug': self.post_slug})

    def __str__(self):
        return '{0}'.format(self.post_title)


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    page_title = models.CharField(max_length=500, help_text='Enter the page title')
    page_content = HTMLField()
    page_thumbnail = models.ImageField(upload_to=upload_image_page, default='no-img.png')
    page_date = models.DateTimeField(auto_now_add=True)
    page_slug = models.SlugField(max_length=200, null=True)


    def admin_display_page_slug(self):
        return '{0}'.format(self.page_slug)

    def get_absolute_url(self):
        return reverse(str(self.post_slug), wargs={'slug': self.post_slug})

    def __str__(self):
        return '{0}'.format(self.page_title)


class SiteOption(models.Model):
    site_option_name = models.CharField(max_length=100, primary_key=True, help_text='Enter unique option name')
    site_option_value = models.TextField(max_length=1000, help_text='Enter the value for the option')


    def admin_display_site_option_value(self):
        return '{0}'.format(self.site_option_value)

    def __str__(self):
        return '{0}'.format(self.site_option_name)


@receiver(post_save, sender=ArchiveProject)
def archive_project_post_save(sender, instance, created, **kwargs):
    if created:
        slug = defaultfilters.slugify('{0}-{1}'.format(instance.project_title[:180], instance.id))
        instance.project_slug = '{0}'.format(slug)
        instance.save()


@receiver(post_save, sender=ArchiveService)
def archive_service_post_save(sender, instance, created, **kwargs):
    if created:
        instance.service_slug = defaultfilters.slugify('{0}-{1}'.format(instance.service_title[:180], instance.id))
        instance.save()


@receiver(post_save, sender=ArchivePost)
def archive_post_post_save(sender, instance, created, **kwargs):
    if created:
        instance.post_slug = defaultfilters.slugify('{0}-{1}'.format(instance.post_title[:180], instance.id))
        instance.save()


@receiver(post_save, sender=Page)
def page_post_save(sender, instance, created, **kwargs):
    if created:
        instance.page_slug = defaultfilters.slugify('{0}'.format(instance.page_title[:180]))
        instance.save()
