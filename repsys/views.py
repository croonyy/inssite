# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from utils.df_to_html import df_to_html

from django.shortcuts import render
from models import RptQuery

from utils import impala_query


# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')


# Create your views here.

def index(request):
    return render(request, 'repsys/index.html')


def layout(request):
    # 取字段唯一值 xxxx.objects.values("field_name").distinct()
    dept_list = RptQuery.objects.values("department").distinct()
    dept_list_t = map(lambda x: x['department'], dept_list)
    query_list = RptQuery.objects.all()
    # print(request.session['username'])
    # print(request.session['password'])
    # print('asdfas df')
    return render(request, 'repsys/layout.html', {"dept_list": dept_list_t, "query_list": query_list})

def get_query(request):

    return HttpResponse()



# unicode是utf8,ascii,gbk的父编码
# 子编码方式到父编码方式只需用[string].decode()
# 父编码方式到子编码方式用[string].encode(encoding='utf8')(其中encoding指定子编码方式)
# 子编码到子编码需要借助父编码unicode编码方式做中转站，不能直接在子编码方式装换。
# 如将ascii编码的string转换成utf8编码：[string].decode().encode(encoding='utf8'))
def querypage(request, rid):
    p1 = rid
    rq1 = RptQuery.objects.get(pk=p1)
    data = impala_query(rq1.query_code.decode().encode(encoding='utf8'))
    # return HttpResponse(u'参数为：%s , %s' % (data[0].to_json(),data[0].to_html()))
    # return HttpResponse(rq1.query_code.decode().encode(encoding='utf8'))
    return HttpResponse(df_to_html(data[0]))


def query_list(request):
    # request.GET.get('key', None)
    query_list = RptQuery.objects.all()
    return render(request, 'repsys/query_list.html', {'query_list': query_list})


def charts(request):
    return render(request, 'repsys/charts.html')


def base(request):
    return render(request, 'repsys/base.html')


@csrf_exempt
def test(request):
    username = request.POST['username']
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    test = request.POST.get('test', "")
    request.session['username'] = username
    request.session['password'] = password
    # request.session.set()
    print(request.session['username'])
    print(request.session['password'])
    return render(request, 'repsys/test.html',
                  {'username': username, 'password': password, 'remember': remember, 'test': test})


def test2(request):
    username = request.session['username']
    # password = request.session['password']
    return HttpResponse(u'username:%s' % username)


def login(request):
    # print(request.session['username'])
    # print(request.session['password'])
    print('asdfas df')
    return render(request, 'repsys/login.html')
