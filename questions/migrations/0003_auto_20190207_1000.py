# Generated by Django 2.1.5 on 2019-02-07 10:00

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
