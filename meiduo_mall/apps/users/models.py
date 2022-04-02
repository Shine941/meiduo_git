from django.db import models

# Create your models here.
# 方法一：
# 自己定义模型
# 密码要加密登录的时候还要实现密码验证
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     mobile =models.CharField(max_length=11, unique=True)

# 方法二：
# Django自带的用户模型User
# 这个用户模型有密码的加密和密码验证
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    class Meta:  # 修改表名
        db_table = 'tb_users'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name