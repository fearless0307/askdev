# Generated by Django 2.1.5 on 2019-02-05 18:16

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20190204_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='storytag',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Tag'),
        ),
    ]
