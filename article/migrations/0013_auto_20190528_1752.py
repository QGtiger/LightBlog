# Generated by Django 2.1.5 on 2019-05-28 17:52

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20190527_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='Carousel', verbose_name='展示图片'),
        ),
    ]