# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import DocumentCategory, Document


# 主页显示所有文档类别 GET
def show_document_category(request):
    doc_cate = DocumentCategory.objects.all().order_by('id')

    return render(request, 'index.html', context=doc_cate)


# 从数据库获取该分类下所有文档信息 GET
def show_document_name(request, doc_cate_id):
    doc = Document.objects.filter(cate=int(doc_cate_id))  # query

    return render(request, 'ShowDocumentCate.html', context=doc)


# 选择文档从数据库调取展示 GET
def show_document(request, doc_id):
    doc = Document.objects.filter(cate=int(doc_id))
    name = doc.name
    content = doc.content
    dict = {
        "doc_name": name,
        "doc_content": content
    }

    return render(request, 'ShowDocument.html', dict)


# 添加分类 POST
def add_document_category(request):
    doc_cate = DocumentCategory()
    doc_cate.name = request.POST.get('name')
    doc_cate.dev_group = request.POST.get('dev_group')
    doc_cate.desc = request.POST.get('desc')
    doc_cate.add_user = request.POST.get('user')
    doc_cate.save()

    return HttpResponse('{"status":"success", "msg":"项目类别添加成功！"}', content_type='application/json')
    # return HttpResponse('{"status":"fail", "msg":"项目类别添加失败！"}', content_type='application/json')


# 添加文档 POST
def add_document(request):
    doc_name = Document()
    doc_name.name = request.POST.get('name')
    doc_name.content = request.POST.get('file')
    doc_name.cate = request.POST.get('doc_cate_id')
    doc_name.desc = request.POST.get('desc')
    doc_name.add_user = request.POST.get('add_user')
    doc_name.save()

    return HttpResponse('{"status":"success", "msg":"文档添加成功！"}', content_type='application/json')


# 删除文档（逻辑删除） GET
def del_document(request, doc_id):
    doc_del_id = doc_id
    doc = Document.objects.get(pk=int(doc_del_id))
    doc.is_del = True

    return HttpResponse('{"status":"success", "msg":"文档删除成功！"}', content_type='application/json')


# 更新原有旧文档 POST
def update_document(request):
    doc_id = request.POST.get('doc_id')
    content = request.POST.get('new_content')
    doc = Document.objects.filter(cate=int(doc_id)).update(content=content)
    doc.save()

    return HttpResponse('{"status":"success", "msg":"文档修改成功！"}', content_type='application/json')
