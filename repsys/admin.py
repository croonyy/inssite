# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import RptQuery, RptUser, RptDataSource

from django.contrib import admin


# Register your models here.
@admin.register(RptQuery)
class ReportQuery_admin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['query_name', 'pk', 'author', 'department', 'short_code', 'short_comment', 'create_time']


# admin.site.register(ReportQuery, ReportQuery_admin)


@admin.register(RptUser)
class ReportQuery_admin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['username', 'password', 'role_code', 'short_comment', 'gender']


@admin.register(RptDataSource)
class ReportQuery_admin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['username', 'password', 'host', 'port', 'dbname', 'describe']
