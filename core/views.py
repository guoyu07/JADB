#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from django.views.generic import View

from core.libs import http


class BaseView(View):
    def __init__(self):
        self.client_ip = http.VerifyIP(self.request.META['REMOTE_ADDR'])

        if not self.client_ip:
            self.client_ip = http.VerifyIP(self.request.META.get(
                'HTTP_X_REAL_IP', '').strip())

        if not self.client_ip:
            self.client_ip = http.VerifyIP(self.request.META.get(
                'HTTP_X_FORWARDED_FOR', '').split(',')[-1].strip())

        if not self.client_ip:
            self.client_ip = '0.0.0.0'

        self.scheme = self.request.META.get(
            'HTTP_X_SCHEME', '').strip() or self.request.scheme

        if self.scheme not in ('http', 'https'):
            self.scheme = 'http'
