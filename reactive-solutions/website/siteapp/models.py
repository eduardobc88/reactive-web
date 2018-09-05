from django.db import models
from django.urls import reverse
from django.template import defaultfilters
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import uuid
import os
from tinymce.models import HTMLField
from colorful.fields import RGBColorField
from django.utils import timezone
from django.utils.safestring import mark_safe


# NOTE: functions to populate the file uploads

def upload_thumbnail_image(instance, filename):
    model_image_prop_name = instance.get_thumbnail_image_prop_name()
    if not hasattr(instance, model_image_prop_name):
        return

    file_name = str(getattr(instance, model_image_prop_name)).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.slide_image = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.slide_image))

def upload_icon_image():
    model_icon_prop_name = instance.get_icon_image_prop_name()
    if not hasattr(instance, model_icon_prop_name):
        return

    file_name = str(getattr(instance, model_icon_prop_name)).split('/')[-1]
    file_ext = file_name.split('.')[-1]
    instance.slide_image = '{0}.{1}'.format(str(uuid.uuid4()), file_ext)
    return os.path.join('siteapp/static/uploads/', str(instance.slide_image))


# NOTE: function to read template file names from path

def get_template_list():
    settings_dir = os.path.dirname(__file__)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
    path = '{0}/templates/page-template/'.format(str(settings_dir))
    list = os.listdir(path)
    choices = [ ('page-template/{0}'.format(template), template.split('.')[0]) for template in list ]
    return choices


# NOTE: start class models

class HomeSlider(models.Model):
    slide_title = models.CharField(max_length=60, help_text='Enter the title')
    slide_content = models.TextField(max_length=150, help_text='Enter the descrition')
    slide_image = models.ImageField(upload_to=upload_thumbnail_image, default='no-img.jpg')


    def get_thumbnail_image_prop_name(self):
        return 'slide_image'

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return '{0}'.format(self.slide_title)


class Banner(models.Model):
    banner_name = models.CharField(max_length=100, primary_key=True, help_text='Enter unique banner name')
    banner_title = models.CharField(max_length=500, help_text='Enter the title for banner')
    banner_content = HTMLField()
    banner_thumbnail = models.ImageField(upload_to=upload_thumbnail_image, default='http://placehold.it/450x350/bfbfbf/ffffff/?text=RW')
    banner_button_name = models.CharField(max_length=100, help_text='Enter the button name')
    banner_button_url = models.CharField(max_length=500, help_text='Enter the button URL')


    def get_thumbnail_image_prop_name(self):
        return 'banner_thumbnail'

    def admin_display_banner_content(self):
        return self.banner_title

    def __str__(self):
        return '{0}'.format(self.banner_name)


class ArchiveProject(models.Model):
    id = models.AutoField(primary_key=True)
    project_title = models.CharField(unique=True, max_length=150, help_text='Enter the project title')
    project_content = HTMLField()
    project_excerpt = models.CharField(max_length=150, null=True, help_text='Enter the project excerpt')
    project_thumbnail = models.ImageField(upload_to=upload_thumbnail_image, default='http://placehold.it/350x450/bfbfbf/ffffff/?text=RW')
    project_slug = models.SlugField(max_length=200, null=True)
    project_created_at = models.DateTimeField(auto_now_add=True)
    project_updated_at = models.DateTimeField(auto_now=True)


    def get_thumbnail_image_prop_name(self):
        return 'project_thumbnail'

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'slug': self.project_slug})

    def class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return '{0}'.format(self.project_title)


class ArchiveService(models.Model):
    id = models.AutoField(primary_key=True)
    service_title = models.CharField(unique=True, max_length=200, help_text='Enter the service title')
    service_content = HTMLField()
    service_excerpt = models.CharField(max_length=150, null=True, help_text='Enter the service excerpt')
    service_thumbnail = models.ImageField(upload_to=upload_thumbnail_image, default='http://placehold.it/1000x600/bfbfbf/ffffff/?text=RW')
    service_icon = models.ImageField(upload_to=upload_icon_image, default='http://placehold.it/500x500/bfbfbf/ffffff/?text=RW')
    service_slug = models.SlugField(max_length=200, null=True)
    service_background_color = RGBColorField(default='#FFFFFF')
    service_created_at = models.DateTimeField(auto_now_add=True)
    service_updated_at = models.DateTimeField(auto_now=True)


    def get_thumbnail_image_prop_name(self):
        return 'service_thumbnail'

    def get_icon_image_prop_name(self):
        return 'service_icon'

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
    post_title = models.CharField(unique=True, max_length=500, help_text='Enter the post title')
    post_content = HTMLField()
    post_excerpt = models.CharField(max_length=150, null=True, help_text='Enter the post excerpt')
    post_thumbnail = models.ImageField(upload_to=upload_thumbnail_image, default='http://placehold.it/350x450/bfbfbf/ffffff/?text=RW')
    post_slug = models.SlugField(max_length=200, null=True)
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_updated_at = models.DateTimeField(auto_now=True)


    def get_thumbnail_image_prop_name(self):
        return 'post_thumbnail'

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
    page_excerpt = models.CharField(max_length=150, null=True, help_text='Enter the page excerpt')
    page_thumbnail = models.ImageField(upload_to=upload_thumbnail_image, default='http://placehold.it/1000x600/bfbfbf/ffffff/?text=RW')
    page_slug = models.SlugField(max_length=200, null=True)
    page_template = models.CharField(max_length=1000, choices=get_template_list(), default='default.html', help_text='Page template')
    page_created_at = models.DateTimeField(auto_now_add=True)
    page_updated_at = models.DateTimeField(auto_now=True)


    def get_thumbnail_image_prop_name(self):
        return 'page_thumbnail'

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
    prospect_created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{0} - {1}'.format(self.prospect_name, self.prospect_email, self.prospect_phone)


# NOTE: start pre save

@receiver(pre_save, sender=ArchivePost)
def archive_post_pre_save(sender, instance, **kwargs):
    instance.post_slug = defaultfilters.slugify('{0}'.format(instance.post_title[:180]))
    slug_exists = ArchivePost.objects.filter(post_slug=str(instance.post_slug))
    if instance.id and slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
        instance.post_slug = defaultfilters.slugify('{0}-{1}'.format(instance.post_title[:180], instance.id))
    if instance.id:
        original_post = ArchivePost.objects.filter(id=instance.id)
        if not original_post:
            return

        instance.post_thumbnail_remove = original_post.values_list('post_thumbnail', flat=True)[0]


@receiver(pre_save, sender=ArchiveProject)
def archive_project_pre_save(sender, instance, **kwargs):
    instance.project_slug = defaultfilters.slugify('{0}'.format(instance.project_title[:180]))
    slug_exists = ArchiveProject.objects.filter(project_slug=str(instance.project_slug))
    if instance.id and slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
        instance.project_slug = defaultfilters.slugify('{0}-{1}'.format(instance.project_slug[:180], instance.id))
    if instance.id:
        original_project = ArchiveProject.objects.filter(id=instance.id)
        if not original_project:
            return

        instance.project_thumbnail_remove = original_project.values_list('project_thumbnail', flat=True)[0]


@receiver(pre_save, sender=ArchiveService)
def archive_service_pre_save(sender, instance, **kwargs):
    instance.service_slug = defaultfilters.slugify('{0}'.format(instance.service_title[:180]))
    slug_exists = ArchiveService.objects.filter(service_slug=str(instance.service_slug))
    if instance.id and slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
        instance.service_slug = defaultfilters.slugify('{0}-{1}'.format(instance.service_title[:180], instance.id))
    if instance.id:
        original_service = ArchiveService.objects.filter(id=instance.id)
        if not original_service:
            return

        instance.service_thumbnail_remove = original_service.values_list('service_thumbnail', flat=True)[0]
        instance.service_icon_remove = original_service.values_list('service_icon', flat=True)[0]


@receiver(pre_save, sender=Page)
def page_pre_save(sender, instance, **kwargs):
    instance.page_slug = defaultfilters.slugify('{0}'.format(instance.page_title[:180]))
    slug_exists = Page.objects.filter(page_slug=str(instance.page_slug))
    if instance.id and slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
        instance.page_slug = defaultfilters.slugify('{0}-{1}'.format(instance.page_title[:180], instance.id))
    if instance.id:
        original_page = Page.objects.filter(id=instance.id)
        if not original_page:
            return

        instance.page_thumbnail_remove = original_page.values_list('page_thumbnail', flat=True)[0]


@receiver(pre_save, sender=Banner)
def banner_pre_save(sender, instance, **kwargs):
    original_banner = Banner.objects.filter(banner_name=instance.banner_name)
    if not original_banner:
        return

    instance.banner_thumbnail_remove = original_banner.values_list('banner_thumbnail', flat=True)[0]


# NOTE: start post save


def delete_file_uploaded(instance, attrname):
    if not hasattr(instance, attrname):
        return

    old_file_path = 'siteapp{0}'.format(getattr(instance, attrname))
    if os.path.isfile(old_file_path):
        os.remove(old_file_path)


@receiver(post_save, sender=HomeSlider)
def home_slider_post_save(sender, instance, created, **kwargs):
    if 'siteapp' in str(instance.slide_image):
        instance.slide_image = str(instance.slide_image).replace('siteapp', '')
        instance.save()


@receiver(post_save, sender=ArchiveProject)
def archive_project_post_save(sender, instance, created, **kwargs):
    save = False
    if created:
        instance.project_slug = defaultfilters.slugify('{0}'.format(instance.project_title[:180]))
        slug_exists = ArchiveProject.objects.filter(project_slug=str(instance.project_slug))
        if slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
            instance.project_slug = defaultfilters.slugify('{0}-{1}'.format(instance.project_title[:180], instance.id))
            save = True
    if 'siteapp' in str(instance.project_thumbnail):
        delete_file_uploaded(instance, 'project_thumbnail_remove')
        instance.project_thumbnail = str(instance.project_thumbnail).replace('siteapp', '')
        save = True
    if save:
        instance.save()


@receiver(post_save, sender=ArchiveService)
def archive_service_post_save(sender, instance, created, **kwargs):
    save = False
    if created:
        instance.service_slug = defaultfilters.slugify('{0}'.format(instance.service_title[:180]))
        slug_exists = ArchiveService.objects.filter(service_slug=str(instance.service_slug))
        if slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
            instance.service_slug = defaultfilters.slugify('{0}-{1}'.format(instance.service_title[:180], instance.id))
            save = True
    if 'siteapp' in str(instance.service_icon):
        delete_file_uploaded(instance, 'service_icon_remove')
        instance.service_icon = str(instance.service_icon).replace('siteapp', '')
        save = True
    if 'siteapp' in str(instance.service_thumbnail):
        delete_file_uploaded(instance, 'service_thumbnail_remove')
        instance.service_thumbnail = str(instance.service_thumbnail).replace('siteapp', '')
        save = True
    if save:
        instance.save()


@receiver(post_save, sender=ArchivePost)
def archive_post_post_save(sender, instance, created, **kwargs):
    save = False
    if created:
        instance.post_slug = defaultfilters.slugify('{0}'.format(instance.post_title[:180]))
        slug_exists = ArchivePost.objects.filter(post_slug=str(instance.post_slug))
        if slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
            instance.post_slug = defaultfilters.slugify('{0}-{1}'.format(instance.post_title[:180], instance.id))
            save = True
    if 'siteapp' in str(instance.post_thumbnail):
        delete_file_uploaded(instance, 'post_thumbnail_remove')
        instance.post_thumbnail = str(instance.post_thumbnail).replace('siteapp', '')
        save = True
    if save:
        instance.save()


@receiver(post_save, sender=Page)
def page_post_save(sender, instance, created, **kwargs):
    save = False
    if created:
        instance.page_slug = defaultfilters.slugify('{0}'.format(instance.page_title[:180]))
        slug_exists = Page.objects.filter(page_slug=str(instance.page_slug))
        if slug_exists.count() and slug_exists.values_list('id', flat=True)[0] != instance.id:
            instance.page_slug = defaultfilters.slugify('{0}-{1}'.format(instance.page_title[:180], instance.id))
            save = True
    if 'siteapp' in str(instance.page_thumbnail):
        delete_file_uploaded(instance, 'page_thumbnail_remove')
        instance.page_thumbnail = str(instance.page_thumbnail).replace('siteapp', '')
        save = True
    if save:
        instance.save()


@receiver(post_save, sender=Banner)
def banner_post_save(sender, instance, created, **kwargs):
    save = False
    if 'siteapp' in str(instance.banner_thumbnail):
        delete_file_uploaded(instance, 'banner_thumbnail_remove')
        instance.banner_thumbnail = str(instance.banner_thumbnail).replace('siteapp', '')
        save = True
    if save:
        instance.save()
