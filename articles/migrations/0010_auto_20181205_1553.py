# Generated by Django 2.1.4 on 2018-12-05 20:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20181204_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cover',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
