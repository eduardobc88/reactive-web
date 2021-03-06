# Generated by Django 2.1 on 2018-10-03 00:28

import colorful.fields
from django.db import migrations, models
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivePost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(help_text='Enter the post title', max_length=500, unique=True)),
                ('post_content', tinymce.models.HTMLField()),
                ('post_excerpt', models.TextField(help_text='Enter the post excerpt', max_length=150, null=True)),
                ('post_thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Thumbnail (1000x400)')),
                ('post_archive_thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Archive thumbnail (350x450)')),
                ('post_slug', models.SlugField(max_length=200, null=True)),
                ('post_created_at', models.DateTimeField(auto_now_add=True)),
                ('post_updated_at', models.DateTimeField(auto_now=True)),
                ('post_status', models.CharField(choices=[('publish', 'Publish'), ('pending', 'Pending'), ('trash', 'Trash')], default='publish', help_text='Chose the status', max_length=30)),
                ('post_author', models.CharField(blank=True, default='', help_text='Enter the author', max_length=200)),
                ('post_keywords', models.TextField(blank=True, default='', help_text="Enter the keywords, example: 'development, code, services'", max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ArchiveProject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(help_text='Enter the project title', max_length=150, unique=True)),
                ('project_content', tinymce.models.HTMLField()),
                ('project_excerpt', models.TextField(help_text='Enter the project excerpt', max_length=150, null=True)),
                ('project_thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Thumbnail (1000x400)')),
                ('project_archive_thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Thumbnail (350x450)')),
                ('project_url', models.CharField(blank=True, help_text='Enter the project URL', max_length=300, null=True)),
                ('project_slug', models.SlugField(max_length=200, null=True)),
                ('project_created_at', models.DateTimeField(auto_now_add=True)),
                ('project_updated_at', models.DateTimeField(auto_now=True)),
                ('project_status', models.CharField(choices=[('publish', 'Publish'), ('pending', 'Pending'), ('trash', 'Trash')], default='publish', help_text='Chose the status', max_length=30)),
                ('project_author', models.CharField(blank=True, default='', help_text='Enter the author', max_length=200)),
                ('project_keywords', models.TextField(blank=True, default='', help_text="Enter the keywords, example: 'development, code, services'", max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ArchiveService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_title', models.CharField(help_text='Enter the service title', max_length=200, unique=True)),
                ('service_content', tinymce.models.HTMLField()),
                ('service_excerpt', models.TextField(help_text='Enter the service excerpt', max_length=150, null=True)),
                ('service_thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Thumbnail (1000x400)')),
                ('service_icon', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Thumbnail (350x350)')),
                ('service_slug', models.SlugField(max_length=200, null=True)),
                ('service_background_color', colorful.fields.RGBColorField(default='#FFFFFF')),
                ('service_created_at', models.DateTimeField(auto_now_add=True)),
                ('service_updated_at', models.DateTimeField(auto_now=True)),
                ('service_status', models.CharField(choices=[('publish', 'Publish'), ('pending', 'Pending'), ('trash', 'Trash')], default='publish', help_text='Chose the status', max_length=30)),
                ('service_author', models.CharField(blank=True, default='', help_text='Enter the author', max_length=200)),
                ('service_keywords', models.TextField(blank=True, default='', help_text="Enter the keywords, example: 'development, code, services'", max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('banner_name', models.CharField(help_text='Enter unique banner name', max_length=100, primary_key=True, serialize=False)),
                ('banner_title', models.CharField(help_text='Enter the title for banner', max_length=500)),
                ('banner_content', models.TextField(help_text='Enter the description', max_length=1000)),
                ('banner_thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Banner image (450x450)')),
                ('banner_button_name', models.CharField(help_text='Enter the button name', max_length=100)),
                ('banner_button_url', models.CharField(help_text='Enter the button URL', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_title', models.CharField(help_text='Enter the title', max_length=60)),
                ('slide_content', models.TextField(help_text='Enter the descrition', max_length=150)),
                ('slide_image', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Slide image (350x350)')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('page_title', models.CharField(help_text='Enter the page title', max_length=500, unique=True)),
                ('page_content', tinymce.models.HTMLField()),
                ('page_excerpt', models.TextField(help_text='Enter the page excerpt', max_length=150, null=True)),
                ('page_thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=500, null=True, verbose_name='Thumbnail (1000x400)')),
                ('page_slug', models.SlugField(max_length=200, null=True)),
                ('page_template', models.CharField(help_text='Page template', max_length=1000)),
                ('page_created_at', models.DateTimeField(auto_now_add=True)),
                ('page_updated_at', models.DateTimeField(auto_now=True)),
                ('page_status', models.CharField(choices=[('publish', 'Publish'), ('pending', 'Pending'), ('trash', 'Trash')], default='publish', help_text='Chose the status', max_length=30)),
                ('page_author', models.CharField(blank=True, default='', help_text='Enter the author', max_length=200)),
                ('page_keywords', models.TextField(blank=True, default='', help_text="Enter the keywords, example: 'development, code, services'", max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prospect_name', models.CharField(max_length=200)),
                ('prospect_last_name', models.CharField(max_length=200)),
                ('prospect_email', models.CharField(max_length=200)),
                ('prospect_phone', models.CharField(max_length=15)),
                ('prospect_website', models.CharField(max_length=200)),
                ('prospect_message', models.TextField(max_length=5000)),
                ('prospect_type', models.CharField(default='Contacto', max_length=50)),
                ('prospect_design_required', models.CharField(default='No', max_length=3)),
                ('prospect_total_pages', models.CharField(default='', max_length=100)),
                ('prospect_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteOption',
            fields=[
                ('site_option_name', models.CharField(help_text='Enter unique option name', max_length=100, primary_key=True, serialize=False)),
                ('site_option_value', models.TextField(help_text='Enter the value for the option', max_length=1000)),
            ],
        ),
    ]
