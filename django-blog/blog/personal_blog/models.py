#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from datetime import datetime
from django.db import models

# Create your models here.


class ColumnModel(models.Model):
    name=models.CharField(max_length=20,verbose_name=u'栏目')
    isDelete=models.BooleanField(default=False)
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'栏目'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class LabelModel(models.Model):
    name=models.CharField(max_length=20,verbose_name=u'标签')
    isDelete=models.BooleanField(default=False)
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'标签'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class ArticleModel(models.Model):
    title=models.CharField(max_length=50,verbose_name=u'标题')
    content=UEditorField(verbose_name=u'文章内容',width=600,height=300, imagePath='images/ueditor/', filePath='images/ueditor/',default='')
    column=models.ForeignKey(ColumnModel,verbose_name=u'所属栏目')
    source=models.CharField(max_length=50,default='admin',verbose_name=u'来源')
    click_nums=models.IntegerField(default=0,verbose_name=u'点击量')
    label=models.ForeignKey(LabelModel,verbose_name=u'标签')
    title_image=models.ImageField(upload_to='media/articles/%Y/%m',max_length=200,default='',verbose_name=u'标题图片')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'发表时间')

    class Meta:
        verbose_name=u'文章'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title


class HomeImageModel(models.Model):
    title=models.CharField(max_length=10,verbose_name=u'主页图片',default='')
    image=models.ImageField(max_length=200,upload_to='media/home/%Y/%m',verbose_name=u'主页图片',default='')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'主页图片'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title


class RecommendModel(models.Model):
    title=models.CharField(max_length=50,verbose_name=u'推荐文章标题',default='')
    recommend=UEditorField(verbose_name=u'推荐文章',default='',width=600,height=300,imagePath='media/recommend/image',filePath='media/recommend/file')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'推荐文章'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title


class SentenceModel(models.Model):
    content=models.TextField(max_length=200,verbose_name=u'每日一句',default='')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'每日一句'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.content


class NoticeModel(models.Model):
    title=models.CharField(max_length=50,verbose_name=u'公告标题',default='')
    content=models.TextField(max_length=500,verbose_name=u'公告内容',default='')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'公告'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title