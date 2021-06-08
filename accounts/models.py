from django.db import models


class CommonModel(models.Model):
    """ 自定义模型的基类 """
    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        # 抽象类，这个类，并不会生成对应的数据库表
        abstract = True


class User(CommonModel):
    """ 用户模型 """
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '帅哥'),
        ('0', '美女'),
    ), default='1')
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    remark = models.CharField('备注', max_length=64, null=True, blank=True)
    email = models.EmailField('用户的邮箱', max_length=64, null=True, blank=True)

    collect_ques = models.ManyToManyField('Question')

    class Meta:
        db_table = 'user'

    def xxx(self):
        pass


class Manager(User):
    class Meta:
        proxy = True

    def xxx(self):
        pass


class Profile(CommonModel):
    """ 用户详细信息 """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile', db_column='user')
    nickname = models.CharField('昵称', max_length=64)


class Question(CommonModel):
    """问题"""
    name = models.CharField('问题名称', max_length=64)


class Answer(CommonModel):
    """答案"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers', verbose_name='关联的问题')


class Classify(models.Model):
    """
    分类
    1. 酒水
        2， 啤酒
        3， 白酒
    """
    name = models.CharField('名称', max_length=64)
    parent = models.ForeignKey('self', related_name='children',
                               on_delete=models.CASCADE)

