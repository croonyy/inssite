from django.conf.urls import url
# from django.contrib import admin
# from django.views.static import serve
# from django.conf import settings
from repsys import views as repsysview
from django.conf import settings

urlpatterns = [
    url(r'^$', repsysview.index,name='index'),
    url(r'^test/$',repsysview.test,name='test'),
    url(r'^test2/$', repsysview.test2, name='test2'),
    url(r'^test-(?P<rid>\d+)/$', repsysview.querypage),
    url(r'^querylist/$', repsysview.query_list),
    url(r'^charts/$',repsysview.charts),
    url(r'^base/$',repsysview.base,name='base'),
    url(r'^login/$',repsysview.login,name='login'),
    url(r'^layout/$',repsysview.layout,name="layout")
]
