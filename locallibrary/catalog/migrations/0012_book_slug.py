# Generated by Django 2.0.7 on 2018-07-16 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20180710_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
