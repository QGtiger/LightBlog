from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column',on_delete=models.CASCADE)
    column = models.CharField(' 栏目 ', max_length=200)
    created = models.DateTimeField(' 创建时间 ', auto_now_add=True)

    def __str__(self):
        return self.column

    class Meta:
        # 如果只设置verbose_name，在Admin中会显示“产品信息 s”
        verbose_name = ' 文章栏目 '
        verbose_name_plural = ' 文章栏目 '


class ArticlePost(models.Model):
    author = models.ForeignKey(User,related_name='article_post',on_delete=models.CASCADE)
    title = models.CharField(' 文章标题 ', max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE,related_name='article_column')
    body = models.TextField(' 文章内容 ')
    created = models.DateTimeField(' 创建时间 ', default=timezone.now)
    updated = models.DateTimeField(' 更新时间 ', auto_now=True)
    users_like = models.ManyToManyField(User, related_name="users_like",blank=True)

    class Meta:
        ordering = ("-updated",)
        index_together = (("id", "slug"),)
        verbose_name = ' 发布的文章 '
        verbose_name_plural = ' 发布的文章 '

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kargs)


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name="comments")
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentator")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    comment_like = models.ManyToManyField(User, related_name="comment_like", blank=True)
    is_read = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name = ' 文章评论 '
        verbose_name_plural = ' 文章评论 '

    def __str__(self):
        return "Comment by {} on {}".format(self.commentator,self.created)