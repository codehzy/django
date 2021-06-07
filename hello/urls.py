from django.urls import path, re_path
from hello.views import hello_world, hello_china, hello_html, article_list, search

urlpatterns = [
    path('world/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
    # 获取url参数
    # path('article/<int:month>', article_list, name='article_list'),
    # 获取url中的正则匹配的参数
    re_path(r'article/(?P<month>0?[1-9]|[012])/$', article_list, name='article_list'),
    # 通过Request对象获取GET参数
    re_path('search', search, name='search')
]
