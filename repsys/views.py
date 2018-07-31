# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from repsys.decorator import login_required

# from utils.df_to_html import df_to_html
from utils.df_to_json import df_to_json

from django.shortcuts import render, redirect
from models import RptQuery, RptUser
from utils import impala_query


# from utils import impala_query


# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')


# Create your views here.

def index(request):
    return render(request, 'repsys/index.html')


def login(request):
    if request.method == "GET":
        # print(request.session['username'])
        # print(request.session['password'])
        # print('asdfas df')
        return render(request, 'repsys/login.html')
    else:
        uname = request.POST['username']
        pwd = request.POST.get('password')
        remember = request.POST.get('remember')

        # 不能用get ，查不到会报错
        try:
            user = RptUser.objects.get(username=uname, password=pwd)
        except:
            wrong = 1
            return render(request, 'repsys/login.html', {'wrong': wrong})
        if user:
            request.session['userid'] = user.pk
            request.session['username'] = uname
            return redirect(reverse('layout'))
        else:
            # 用来在登录页面显示登录失败
            wrong = 1
            return render(request, 'repsys/login.html', {'wrong': wrong})


# def login_validate(request):
#     uname = request.POST['username']
#     pwd = request.POST.get('password')
#     remember = request.POST.get('remember')
#
#     # 不能用get ，查不到会报错
#     user = RptUser.objects.filter(username=uname, password=pwd)
#     if user:
#         request.session['username'] = uname
#         return redirect(reverse('layout'))
#     else:
#         # 用来在登录页面显示登录失败
#         wrong = 1
#         return render(request, 'repsys/login.html', {'wrong': wrong})


def logout(request):
    if request.session.has_key('username'):
        del request.session["username"]
        return redirect(reverse('login'))
    else:
        return redirect(reverse('login'))


# @login_required
@login_required
def layout(request):
    # 取字段唯一值 xxxx.objects.values("field_name").distinct()
    dept_list = RptQuery.objects.values("department").distinct()
    dept_list_t = map(lambda x: x['department'], dept_list)
    query_list = RptQuery.objects.all()
    print(request.session['username'])
    # print(request.session['password'])
    # print('asdfas df')
    return render(request, 'repsys/layout.html', {"dept_list": dept_list_t, "query_list": query_list})


@login_required
def get_query(request, rid):
    p1 = rid  # 获取查询id
    print(p1)
    rq1 = RptQuery.objects.get(pk=p1)
    name_dict = {'rid': rq1.pk, 'rname': rq1.query_name, 'rauthor': rq1.author,
                 'rdept': rq1.department, 'rcode': rq1.query_code, 'rcmt': rq1.comment}
    return JsonResponse(name_dict)


# @csrf_exempt
# @login_required
def savequery(request):
    userid = request.session["userid"]
    # print(userid)
    # if request.POST:
    if request.POST.get('rid'):
        rq1 = RptQuery.objects.get(pk=request.POST.get('rid'))
    else:
        rq1 = RptQuery()
    rq1.query_name = request.POST.get('rname')
    rq1.author = request.POST.get('rauthor')
    rq1.department = request.POST.get('rdept')
    rq1.query_code = request.POST.get('rcode')
    rq1.comment = request.POST.get('rcmt')
    rq1.userid = RptUser.objects.get(pk=userid)
    try:
        rq1.save()
        return JsonResponse({'status': 0})
    except Exception, e:
        return JsonResponse({'status': 1, 'except': str(e)})
    # else:
    #     return JsonResponse({'status': 1, 'except': '提交请求出错，请重试！'})


def exequery(request):
    try:
        e_code = request.POST.get('code')
        q_result = impala_query('yangyuan', 'yangyuan', e_code)
        data = df_to_json(q_result[0])
        return JsonResponse(data, safe=False)
    except Exception, e:
        return JsonResponse({'status': 1, 'except': str(e)})


def del_query(request):
    try:
        q_id = request.POST.get('q_id')
        q = RptQuery.objects.get(pk=q_id)
        q.delete()
        return JsonResponse({'status': 0})
    except Exception, e:
        return JsonResponse({'status':1,'except':str(e)})


# 以下是测试
def ajax_add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))


def ajax_list(request):
    # a = [
    #     {'aaa': 4, 'b': 8},
    #     {'bbb': 3, 'b': 6}]
    # b=str(a).encode(encoding='utf-8')
    s = '''
    select
    a.listing_id
    ,a.user_id
    ,a.amount
    ,a.status
    ,a.is_pay
    from
    edw.cmn_listing a
    where 
    a.auditing_date>'2018-07-25'
    limit 10
    '''
    data_tmp = impala_query('yangyuan', 'yangyuan', s)
    data = df_to_json(data_tmp[0])
    print(type(data))
    # print(data)
    return JsonResponse(data, safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)


# unicode是utf8,ascii,gbk的父编码
# 子编码方式到父编码方式只需用[string].decode()
# 父编码方式到子编码方式用[string].encode(encoding='utf8')(其中encoding指定子编码方式)
# 子编码到子编码需要借助父编码unicode编码方式做中转站，不能直接在子编码方式装换。
# 如将ascii编码的string转换成utf8编码：[string].decode().encode(encoding='utf8'))
# def querypage(request, rid):
#     p1 = rid
#     rq1 = RptQuery.objects.get(pk=p1)
#     data = impala_query(rq1.query_code.decode().encode(encoding='utf8'))
#     data_m = df_to_html(data[0])
#     # return HttpResponse(u'参数为：%s , %s' % (data[0].to_json(),data[0].to_html()))
#     # return HttpResponse(rq1.query_code.decode().encode(encoding='utf8'))
#     return HttpResponse(data_m)


# def query_list(request):
#     # request.GET.get('key', None)
#     query_list = RptQuery.objects.all()
#     return render(request, 'repsys/query_list.html', {'query_list': query_list})


# def charts(request):
#     return render(request, 'repsys/charts.html')


# def base(request):
#     return render(request, 'repsys/base.html')


# @csrf_exempt
# def test(request):
#     username = request.POST['username']
#     password = request.POST.get('password')
#     remember = request.POST.get('remember')
#     test = request.POST.get('test', "")
#     request.session['username'] = username
#     request.session['password'] = password
#     # request.session.set()
#     print(request.session['username'])
#     print(request.session['password'])
#     return render(request, 'repsys/test.html',
#                   {'username': username, 'password': password, 'remember': remember, 'test': test})


# def test2(request):
# username = request.session['username']
# password = request.session['password']
# return HttpResponse(u'username:%s' % username)
# return render(request,'repsys/test2.html')


# def test3(request):
# password = request.session['password']
# return render(request, 'repsys/test3.html')


def test4(request):
    # password = request.session['password']
    return render(request, 'repsys/test4.html')


def test5(request):
    # password = request.session['password']
    return render(request, 'repsys/test5.html')


def test6(request):
    # password = request.session['password']
    return render(request, 'repsys/test6.html')


def base(request):
    # password = request.session['password']
    return render(request, 'repsys/base.html')


def base2(request):
    # password = request.session['password']
    return render(request, 'repsys/base2.html')
