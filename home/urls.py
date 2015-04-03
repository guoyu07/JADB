#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from django.conf.urls import url

urlpatterns = [
    url(r'^.*$', 'home.views.index')
]
