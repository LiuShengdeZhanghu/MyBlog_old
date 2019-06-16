from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    # models.CASCADE 联级删除，比如删除user，也会把该User评论的内容删除，但是删除comment时候也不会删除user，比较合理
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    #contentpye 对Django的数据库模型中的进行关联

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name="comments", on_delete=models.CASCADE)

    #评论下的回复的最顶级的
    root = models.ForeignKey('self',related_name="root_comment",null=True,on_delete=models.CASCADE)
    # 评论回复功能的上一级s是谁
    parent = models.ForeignKey('self',related_name="parent_comment",null=True,on_delete=models.CASCADE)
    # 回复的对象，这里设置了两个关联到User的外键，为了你能够反向解析出（用User找出该用户的所有评论），对反向解析的目标字段进行修改
    reply_to = models.ForeignKey(User,related_name="replies",null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    #让评论时间最新的在最上面
    class Meta():
        ordering = ['comment_time']
