# -*- coding: utf-8 -*-
from django.conf.urls import url
from .import views



urlpatterns=[
    # 调取所有分类
    url(r'^show_document_category$',views.show_document_category),
    # 调取所有文档名
    url(r'^show_document_name$',views.show_document_name),
    # 调取指定文档
    url(r'^show_document_(\d+)$',views.show_document),
    # 增加文档分类
    url(r'^add_document_category$',views.show_document_category),
    # 上传文档
    url(r'^add_document$',views.add_document),
    # 删除指定文档
    url(r'^del_document_(\d+)$',views.del_document),
    # 更新文档
    url(r'^update_document$',views.update_document),

]