# Generated by Django 2.1 on 2018-08-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0014_prospect'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivepost',
            name='post_excerpt',
            field=models.CharField(help_text='Enter the post excerpt', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_template',
            field=models.CharField(choices=[('page-template/template-privacy.html', 'template-privacy'), ('page-template/template-thankyou.html', 'template-thankyou'), ('page-template/template-default.html', 'template-default'), ('page-template/template-contact.html', 'template-contact')], default='default.html', help_text='Page template', max_length=1000),
        ),
    ]
