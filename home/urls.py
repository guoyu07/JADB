#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.conf.urls import url

from home.views import HomeView

urlpatterns = [
    url(r'^.*$', HomeView.as_view())
]
