# Generated by Django 2.1.5 on 2019-02-08 05:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20190207_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]