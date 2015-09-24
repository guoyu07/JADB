#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.conf.urls import include, url


urlpatterns = [
    url(r'^account/', include('account.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^', include('home.urls'))
]
