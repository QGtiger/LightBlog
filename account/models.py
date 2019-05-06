from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    school = models.CharField(' 学校 ',max_length=100,blank=True)
    company = models.CharField(' 在职公职 ',max_length=100,blank=True)
    profession = models.CharField(' 工作 ',max_length=100,blank=True)
    address = models.CharField(' 地址 ',max_length=100,blank=True)
    aboutme = models.TextField(' 自我介绍 ',blank=True)
    photo = models.ImageField(' 头像 ', blank=True)

    def __str__(self):
        return "User:{}".format(self.user.username)

    class Meta:
        # 如果只设置verbose_name，在Admin中会显示“产品信息 s”
        verbose_name = ' 用户信息 '
        verbose_name_plural = ' 用户信息 '
