#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.conf.urls import url

from home.views import HomeView

year = r'^(?P<year>\d{4})'
month = r'/(?P<month>\d{2})'
day = r'/(?P<day>\d{2})'
page = r'/(?:page-(?P<page>\d+))?$'

urlpatterns = [
    url(year + month + day + page, HomeView.as_view()),
    url(year + month + page, HomeView.as_view()),
    url(year + page, HomeView.as_view()),
    url(r'^$', HomeView.as_view())
]
