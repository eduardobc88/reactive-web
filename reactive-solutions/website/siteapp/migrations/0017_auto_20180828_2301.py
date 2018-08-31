# Generated by Django 2.1 on 2018-08-28 23:01

from django.db import migrations, models
import siteapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0016_auto_20180824_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivepost',
            name='post_thumbnail',
            field=models.ImageField(default='/static/img/350x450.png', upload_to=siteapp.models.upload_image_post),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_template',
            field=models.CharField(choices=[('page-template/template-thankyou.html', 'template-thankyou'), ('page-template/template-default.html', 'template-default'), ('page-template/template-contact.html', 'template-contact')], default='default.html', help_text='Page template', max_length=1000),
        ),
    ]