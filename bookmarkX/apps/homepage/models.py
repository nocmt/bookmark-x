from django.db import models
from django.utils import timezone


# Create your models here.


# 用户表
class Users(models.Model):
    username = models.EmailField(verbose_name='账号')
    password = models.CharField(max_length=78, verbose_name='密码')
    addTime = models.DateTimeField(default=timezone.now, verbose_name='时间')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    # 时间格式化
    @property
    def EaddTime(self):
        return self.addTime.strftime('%Y-%m-%d %H:%M')


# 分类表
class Sort(models.Model):
    # 表示外键关联到用户表,当用户表删除了该条数据, 分类表中删除
    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField(max_length=50, verbose_name='分类名称')
    addTime = models.DateTimeField(default=timezone.now, verbose_name='时间')
    isEnable = models.BooleanField(default=True, verbose_name='是否启用')

    class Meta:
        verbose_name = '书签分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 时间格式化
    @property
    def EaddTime(self):
        return self.addTime.strftime('%Y-%m-%d %H:%M')


# 书签表
class Bookmarks(models.Model):
    # 表示外键关联到用户表,当用户表删除了该条数据, 分类表中删除
    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE, verbose_name='用户')
    title = models.CharField(max_length=50, verbose_name='名称')
    link = models.CharField(max_length=500, verbose_name='链接')
    imgUrl = models.CharField(max_length=300, blank=True, null=True, verbose_name='封面')
    sort = models.ForeignKey(Sort, null=True, blank=True, on_delete=models.CASCADE, verbose_name='分类')
    addTime = models.DateTimeField(default=timezone.now, verbose_name='时间')
    isInvalid = models.BooleanField(default=False, verbose_name='是否失效')

    class Meta:
        verbose_name = '书签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # 分类外键格式化
    @property
    def sortName(self):
        return self.sort.name

    # 时间格式化
    @property
    def EaddTime(self):
        return self.addTime.strftime('%Y-%m-%d %H:%M')
