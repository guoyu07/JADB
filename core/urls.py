#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from core.libs import utility
from django.conf.urls import include, url

urlpatterns = [
    url(r'^%s\.html$' % utility.allowed_characters, include('article.urls')),
    url(r'^.*$', include('home.urls')),
]
