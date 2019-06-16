"""talkrobot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from robot import views

urlpatterns = [
    #localhost:8000/article/
    path('', views.article_list, name="article_list"),
    path('<int:article_id>', views.article_detail, name='article_detail'),
    path('type/<int:blog_type_pk>',views.blogs_with_type,name='blog_with_type'),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name='blog_with_date'),
    # path('login/',views.blog_login,name='blog_login'),
    # path('login_for_medal',views.login_for_medal,name='login_for_medal'),
    # path('register',views.blog_register,name="blog_register"),
    path('home',views.home),
    path('talk/',views.talk),
]
