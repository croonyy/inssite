# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-19 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repsys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rptquery',
            old_name='report_name',
            new_name='query_name',
        ),
    ]
