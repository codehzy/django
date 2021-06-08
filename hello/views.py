# coding:utf-8
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import FileResponse

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse


def hello_world(request):
    return HttpResponse('hello world')


def hello_china(request):
    return HttpResponse('hello china')


def hello_html(request):
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>
        </body>
    </html>
    """
    return HttpResponse(html)


def article_list(request, month):
    """
    :param month: 今年某一个月的文章列表
    """
    return HttpResponse('article:{}'.format(month))


def search(request):
    """GET参数获取"""
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功')


def render_str(request):
    """render_to_string函数使用"""
    templ_name = 'index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)


def render_html(request):
    """render_to_string函数使用"""
    return render(request, 'index.html')


def http_request(request):
    """请求练习"""
    # 1. 请求方式
    print(request.method)
    # 2. 请求头信息
    headers = request.META
    print(headers)
    ua = request.META.get("HTTP_USER_AGENT", None)
    print(ua)
    print(request.headers)
    print(request.headers['user-agent'])
    # 3. 获取请求参数
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('响应')


def http_response(request):
    """响应练习"""
    # resp = HttpResponse('响应内容', status=201)
    # resp.status_code = 204
    # print(resp.status_code)
    # return resp

    # JSON
    # user_info = {
    #     "name":"张三",
    #     "age":34
    # }
    # return JsonResponse(user_info)

    response = FileResponse(open('text.txt','rb'))
    return response
