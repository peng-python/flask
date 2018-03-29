#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserModel(AbstractUser):
    nick_name=models.CharField(max_length=50,default='',verbose_name=u'昵称')
    mobile=models.CharField(max_length=11,default='',verbose_name=u'手机号码')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'用户信息'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username