# Generated by Django 2.1.5 on 2019-02-04 10:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
