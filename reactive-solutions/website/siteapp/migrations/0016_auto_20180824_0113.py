# Generated by Django 2.1 on 2018-08-24 01:13

from django.db import migrations, models
import siteapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0015_auto_20180823_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='archiveproject',
            name='project_excerpt',
            field=models.CharField(help_text='Enter the project excerpt', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='archiveservice',
            name='service_excerpt',
            field=models.CharField(help_text='Enter the service excerpt', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='page_excerpt',
            field=models.CharField(help_text='Enter the page excerpt', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='archivepost',
            name='post_thumbnail',
            field=models.ImageField(default='http://placehold.it/350x450/7b7b7b/DADADA/?text=350x450', upload_to=siteapp.models.upload_image_post),
        ),
        migrations.AlterField(
            model_name='archiveproject',
            name='project_thumbnail',
            field=models.ImageField(default='http://placehold.it/350x450/7b7b7b/DADADA/?text=350x450', upload_to=siteapp.models.upload_image_project),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_thumbnail',
            field=models.ImageField(default='http://placehold.it/1000x600/7b7b7b/DADADA/?text=1000x600', upload_to=siteapp.models.upload_image_page),
        ),
    ]
