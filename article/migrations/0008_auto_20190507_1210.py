# Generated by Django 2.1.5 on 2019-05-07 12:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_comment_is_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecolumn',
            options={'verbose_name': ' 文章栏目 ', 'verbose_name_plural': ' 文章栏目 '},
        ),
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-updated',), 'verbose_name': ' 发布的文章 ', 'verbose_name_plural': ' 发布的文章 '},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': ' 文章评论 ', 'verbose_name_plural': ' 文章评论 '},
        ),
        migrations.AddField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='column',
            field=models.CharField(max_length=200, verbose_name=' 栏目 '),
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=' 创建时间 '),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=models.TextField(verbose_name=' 文章内容 '),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=' 创建时间 '),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='title',
            field=models.CharField(max_length=200, verbose_name=' 文章标题 '),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name=' 更新时间 '),
        ),
    ]
