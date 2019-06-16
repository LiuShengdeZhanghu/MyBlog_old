from django.db import models
from django.utils import timezone
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from read_statistics.models import ReadNum,ReadDetail
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpand

# Create your models here.

#博客的分类，可能一篇博客有多个分类,外键必须在前面的类中出现
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Article(models.Model,ReadNumExpand):
    # 继承的ReadNumExpand
    title = models.CharField(max_length=20,verbose_name="题目")
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE,default=1)
    content = RichTextUploadingField()
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    #新添加一个字段的时i候会出现需要默认值的情况，这里为自动添加创建的时间
    last_updated_time = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1,verbose_name="作者")
    # 这里的user是admin的超级管理员
    is_deleted = models.BooleanField(default=False,verbose_name="是否删除")
    read_details = GenericRelation(ReadDetail)
    #关联到ReadDetail模型
    def __str__(self):
        #定制修改
        return "Article: %s"%self.title
    '''
    #adminxd的
        def read_num(self):
        #取出阅读的数量
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0
    '''
    #admin的 拓展到read_statistics.models的ReadNumExpand
    # def read_num(self):
    #     try:
    #         ct = ContentType.objects.get_for_model(Article)
    #         blog_id = self.pk
    #         read_num = ReadNum.objects.get(content_type=ct,object_id=blog_id)
    #         return read_num.read_num
    #     except exceptions.ObjectDoesNotExist:
    #         return 0

    #设置分页时的排序
    class Meta:
        ordering = ['-create_time']

'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0,verbose_name="阅读数量")
    blog = models.OneToOneField(Article,on_delete=models.DO_NOTHING) #一对一的外键关系

    def __str__(self):
        #定制修改
        return "博客阅读数量"
'''


#python manage.py makemigrations python manage.py migrate
#   通过这两条同步