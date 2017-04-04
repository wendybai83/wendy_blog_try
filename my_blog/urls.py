# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),  #可以使用设置好的url进入网站后台
    #url(r'^test/$', 'article.views.test'),
    url(r'^$', 'article.views.home'),
    url(r'^([0-9]+)/$', 'article.views.detail', name='detail'),
    #url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
)
