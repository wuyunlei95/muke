import json

from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.core.serializers.json import json


# Create your views here.
def index(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'Login.HTML')

    # 存放用户输入数据的字典列表

inptDicLst = [
    # 存放一些原始数据
    {'usr': '1234', 'pwd': '1234'}
]
def Login1(request):
    '''
    POST请求
    我好难啊，搞了我老半天
    :param request:
    :return:
    '''
    # return HttpResponse(request, 'Login.HTML')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # return HttpResponse('THIS IS TEST')

        return redirect('https://www.baidu.com') # redirect重定向
    else:
        return render(request, 'Login.HTML', {'lst': inptDicLst})
        # return render(request, 'Login.HTML')


def Login2(request):
    '''
    GET请求
    :param request:
    :return:
    '''
    if request.method == 'GET':
        username = request.GET.get('username')

        password = request.GET.get('username')
        return HttpResponse(username,password)
    else:
        return render(request, 'Login.HTML')


def Login3(request):
    '''
    處理請求數據
    GET时将if request.method == 'GET':，将两段注释放开
    中文编码问题，'中国' 中的ascii 字符码，而不是真正的中文。
    这是因为json.dumps 序列化时对中文默认使用的ascii编码.
    想输出真正的中文需要指定ensure_ascii=False：
    :param request:
    :return:
    '''

    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        # data = request.POST.get('data')
        result['username'] = username
        result['pd'] = password
        # result['data'] = data
        result = json.dumps(result,ensure_ascii=False)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render(request, 'Login.HTML')






def Login4(request):
    '''
    處理請求數據
    GET时将if request.method == 'GET':，将两段注释放开
    中文编码问题，'中国' 中的ascii 字符码，而不是真正的中文。
    这是因为json.dumps 序列化时对中文默认使用的ascii编码.
    想输出真正的中文需要指定ensure_ascii=False：
    :param request:
    :return:
    '''

    if request.method == 'POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        # data = request.POST.get('data')
        result['username'] = username
        result['pd'] = password
        # result['data'] = data
        result = json.dumps(result,ensure_ascii=False)
        return HttpResponse(result,content_type='application/json;charset=utf-8')
    else:
        return render(request, 'Login.HTML')