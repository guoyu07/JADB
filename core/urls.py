#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    #url(r'^%s\.html$' % settings.ALLOWED_CHARACTERS, include('article.urls')),
    url('', include('home.urls'))
]
