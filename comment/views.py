from django.shortcuts import render,redirect
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .forms import CommentForm
# Create your views here.

def update_comment(request):
    # 返回当前页面
    '''referer = request.META.get('HTTP_REFERER', reverse('index'))
    user = request.user
    if not user.is_authenticated:
        return render(request, 'error.html', {'message': '没有登录用户','redirect_to':referer})

    text = request.POST.get('text','').strip()
    if text == "":
        return render(request,'error.html',{'message':'不能提交空的信息','redirect_to':referer})

    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        # 通过contenttype得到评论的对象（博客）
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'error.html', {'message': str(e)+"评论对象不存在",'redirect_to':referer})

    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = model_obj
    comment.save()

    return redirect(referer)'''
    referer = request.META.get('HTTP_REFERER', reverse('index'))
    comment_form = CommentForm(request.POST, user = request.user)
    if comment_form.is_valid():
        # 数据检查通过，保存评论
        comment = Comment()
        comment.user = request.user
        comment.text = comment_form.cleaned_data["text"]
        comment.content_object = comment_form.cleaned_data["content_object"]
        comment.save()
        return redirect(referer)

    else:
        return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
