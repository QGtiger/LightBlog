from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userinfo',  unique=True)
    school = models.CharField(' 学校 ',max_length=100,blank=True)
    company = models.CharField(' 在职公职 ',max_length=100,blank=True)
    profession = models.CharField(' 工作 ',max_length=100,blank=True)
    address = models.CharField(' 地址 ',max_length=100,blank=True)
    aboutme = models.TextField(' 自我介绍 ',blank=True)
    photo = models.ImageField(' 头像 ',upload_to='avator', default='default/default.jpg')

    # 注意：ImageSpecField不会生成数据库中的表
    # 处理后的图片
    photo_150x150 = ImageSpecField(
        source="photo",
        processors=[ResizeToFill(30, 30)], # 处理后的图像大小
        format='JPEG',  # 处理后的图片格式
        options={'quality': 95} # 处理后的图片质量
        )

    def __str__(self):
        return "User:{}".format(self.user.username)

    class Meta:
        # 如果只设置verbose_name，在Admin中会显示“产品信息 s”
        verbose_name = ' 用户信息 '
        verbose_name_plural = ' 用户信息 '
