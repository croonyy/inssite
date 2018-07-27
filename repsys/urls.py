# coding=utf-8
from django.conf.urls import url
# from django.contrib import admin
# from django.views.static import serve
# from django.conf import settings
from repsys import views as repsysviews
from django.conf import settings

urlpatterns = [
    url(r'^$', repsysviews.index, name='index'),
    url(r'^login/$', repsysviews.login, name='login'),
    url(r'^login_validate/$', repsysviews.login_validate, name='login_validate'),
    url(r'^logout/$', repsysviews.logout, name='logout'),
    url(r'^layout/$', repsysviews.layout, name="layout"),
    url(r'^getquery-(?P<rid>\d+)/$', repsysviews.get_query,name='get_query'),
    url(r'^savequery/$', repsysviews.savequery,name='savequery'),

    # 以下是ajax测试

    url(r'^ajax_add/$', repsysviews.ajax_add, name='ajax_add'),
    url(r'^ajax_list/$', repsysviews.ajax_list, name='ajax_list'),
    url(r'^ajax_dict/$', repsysviews.ajax_dict, name='ajax_dict'),

    # url(r'^query-(?P<rid>\d+)/$', repsysviews.querypage,name='querypage'),

    url(r'^base/$', repsysviews.base, name='base'),
    url(r'^base2/$', repsysviews.base2, name='base2'),



    # url(r'^test/$', repsysviews.test, name='test'),
    # url(r'^test2/$', repsysviews.test2, name='test2'),

    # url(r'^test3/$', repsysviews.test3, name='test3'),
    url(r'^test4/$', repsysviews.test4, name='test4'),
    url(r'^test5/$', repsysviews.test5, name='test5'),
    # url(r'^add/$', repsysviews.test3, name='add'),

    # url(r'^querylist/$', repsysviews.query_list),
    # url(r'^charts/$', repsysviews.charts),
    # url(r'^base/$', repsysviews.base, name='base'),
]
