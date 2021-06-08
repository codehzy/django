from django.db import models


class User(models.Model):
    """ 用户模型 """
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', 'male'),
        ('2', 'female')
    ), default=1)
    age = models.PositiveIntegerField("年龄", default=0)
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    remark = models.CharField('备注', max_length=64, null=True, blank=True)

    created_at = models.DateTimeField("注册时间", auto_now_add=True)
    updated_at = models.DateTimeField("最后修改时间", auto_now=True)
