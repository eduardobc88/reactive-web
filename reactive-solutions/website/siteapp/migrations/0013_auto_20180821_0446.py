# Generated by Django 2.1 on 2018-08-21 04:46

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0012_archiveproject_project_background_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archiveproject',
            name='project_background_color',
        ),
        migrations.AddField(
            model_name='archiveservice',
            name='service_background_color',
            field=colorful.fields.RGBColorField(default='#FFFFFF'),
        ),
    ]
