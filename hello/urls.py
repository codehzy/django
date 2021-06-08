from django.urls import path, re_path
from hello.views import hello_world, hello_china, hello_html, article_list, search, render_str, render_html, \
    http_request, http_response, article_detail, no_data_404, HomeView

urlpatterns = [
    path('world/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    path('html/', hello_html, name='hello_html'),
    # 获取url参数
    # path('article/<int:month>', article_list, name='article_list'),
    # 获取url中的正则匹配的参数
    # re_path(r'article/(?P<month>0?[1-9]|[012])/$', article_list, name='article_list'),
    # 通过Request对象获取GET参数
    re_path('search', search, name='search'),
    re_path('render/str', render_str, name='render_str'),
    re_path('render/html', render_html, name='render_html'),
    re_path('http/req', http_request, name='http_request'),
    re_path('http/rep', http_response, name='http_response'),
    re_path('404/', no_data_404,  name='no_data_404'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    re_path('home/', HomeView.as_view(), name='HomeView')
]
