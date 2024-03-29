#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author: liusheng time:2019/5/3
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

class loginForm(forms.Form):
    username = forms.CharField(label="用户名", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"用户名"}), required=True)   #默认为True
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class':'form-control',"placeholder":"用户密码"}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            # Django提供的form的错误信息接口
            raise forms.ValidationError('用户名或者密码不正确')
        else:
            #写回user
            self.cleaned_data["user"] = user
        return self.cleaned_data

class RegForm(forms.Form):
    username = forms.CharField(label="用户名",max_length="30",min_length=3,
                               widget=forms.TextInput(attrs={"class":"form-control","placeholder":"输入3-30之间的用户名"}), required=True)
    email = forms.EmailField(label="用户邮箱",
                             widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"填写用户邮箱"}), required=True)
    verification_code = forms.CharField(label="验证码",
                               widget=forms.TextInput(attrs={"class":"form-control","placeholder":"点击“发送验证码”"}))
    password = forms.CharField(label="设置密码", min_length=6,
                               widget=forms.PasswordInput(attrs={'class':'form-control',"placeholder":"设定用户密码"}))
    password_again = forms.CharField(label="再输入一次密码",min_length=6,
                                     widget=forms.PasswordInput(attrs={'class':'form-control',"placeholder":"再次输入用户密码"}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists() > 0:
            raise forms.ValidationError("用户名已经存在！")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists() > 0:
            raise forms.ValidationError("该邮箱已经注册过！")
        return email

    def clean_password_again(self):
        password_again = self.cleaned_data['password_again']
        password = self.cleaned_data['password']
        if password != password_again:
            raise forms.ValidationError("两次输入的密码不相同！")
        return password_again


class ChangeNicknameForm(forms.Form):
    nickname_new = forms.CharField(label="新的昵称",max_length=20,
                               widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入新的昵称"}), required=True)

    def __init__(self,*args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ChangeNicknameForm,self).__init__(*args, **kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data["user"] = self.user
        else:
            raise forms.ValidationError("用户尚未登录")
        return self.cleaned_data

    def clean_nickname_new(self):
        nickname_new = self.cleaned_data.get('nickname_new','').strip()  # 去掉前后空格
        if nickname_new == '':
            raise forms.ValidationError("新的昵称不能为空")
        return nickname_new

class BindEmailForm(forms.Form):
    email = forms.EmailField(label="邮箱",
                               widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"请注册的邮箱"}))
    verification_code = forms.CharField(label="验证码",
                               widget=forms.TextInput(attrs={"class":"form-control","placeholder":"点击“发送验证码”"}))

    def __init__(self,*args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        super(BindEmailForm,self).__init__(*args, **kwargs)

    def clean(self):
        # 判断用户是否登录
        if self.request.user.is_authenticated:
            self.cleaned_data["user"] = self.request.user
        else:
            raise forms.ValidationError("用户尚未登录")
        # 判断用户是否绑定邮件
        if self.request.user.email != '':
            raise forms.ValidationError('你已经绑定过邮箱')

        # 判断验证码
        code = self.request.session.get('bind_email_code','')
        verification_code = self.cleaned_data.get('verification_code','')

        if not (code != '' and code == verification_code):
            raise forms.ValidationError('验证码不正确')
        return self.cleaned_data

    def clean_email(self):
        # 判断接收验证码的邮箱和提交上来的邮箱是否一致
        email_old = self.request.session.get('email', '')
        email = self.cleaned_data['email']
        if email != email_old:
            raise forms.ValidationError('接收验证码的邮箱和绑定的邮箱不一致')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已经绑定')
        return email

    def clean_verification_code(self):
        verification_code = self.cleaned_data.get('verification_code').strip()
        if verification_code == '':
            raise forms.ValidationError('验证码不能为空')
        return verification_code