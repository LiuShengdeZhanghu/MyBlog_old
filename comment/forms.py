#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author: liusheng time:2019/5/4
from django import forms
from django.db.models import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput())
    object_id = forms.IntegerField(widget=forms.HiddenInput())
    # 对评论框使用Django的框架渲染为富文本
    text = forms.CharField(widget=CKEditorWidget(config_name="comment_ckeditor"))

    def __init__(self,*args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm,self).__init__(*args, **kwargs)
        pass

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data["user"] = self.user
        else:
            raise forms.ValidationError("用户尚未登录")
        # 评论对象判断验证
        content_type = self.cleaned_data["content_type"]
        object_id = self.cleaned_data["object_id"]
        # 通过contenttype得到评论的对象（博客）
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data["content_object"] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError("评论对象不存在")
        return self.cleaned_data