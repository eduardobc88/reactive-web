# Generated by Django 2.1 on 2018-08-08 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0009_auto_20180808_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_template',
            field=models.CharField(blank=True, choices=[('default', 'default.html'), ('template-privacy', 'template-privacy.html'), ('template-contact', 'template-contact.html')], default='default.html', help_text='Page template', max_length=1000),
        ),
    ]