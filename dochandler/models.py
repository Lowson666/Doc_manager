from django.db import models

# Create your models here.


class DocumentCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='分类名')
    dev_group = models.CharField(max_length=64, blank=True, null=True, verbose_name='开发团队Leader')
    desc = models.TextField(blank=True, null=True, verbose_name='项目分类说明')
    add_user = models.CharField(max_length=64,null=True, verbose_name='添加者')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

class Document(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='文档名')
    content = models.TextField(verbose_name='文章正文')
    cate = models.ForeignKey(DocumentCategory, verbose_name='所属分类',on_delete=models.CASCADE)
    desc = models.TextField(blank=True, null=True, verbose_name='文档说明')
    add_user = models.CharField(max_length=64,null=True, verbose_name='添加者')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    is_del = models.BooleanField(default=False, verbose_name='逻辑删除')


