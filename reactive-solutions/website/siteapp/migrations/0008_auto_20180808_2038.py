# Generated by Django 2.1 on 2018-08-08 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0007_auto_20180808_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archiveproject',
            old_name='slug',
            new_name='project_slug',
        ),
    ]