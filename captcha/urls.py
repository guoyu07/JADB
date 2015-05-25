#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.conf.urls import url

from captcha.views import CaptchaView


urlpatterns = [
    url('', CaptchaView.as_view())
]
