# Generated by Django 2.1.5 on 2019-05-07 14:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20190507_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name=' 文章内容 '),
        ),
    ]