# Generated by Django 2.1 on 2018-09-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='page_date',
            new_name='page_created_at',
        ),
        migrations.AddField(
            model_name='page',
            name='page_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
