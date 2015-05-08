#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.views.generic import View

from core import Core
from core.libs import http


class BaseView(View, Core):
    Core = Core

    def dispatch(self, *args, **kwargs):
        self.client_ip = http.VerifyIP(self.request.META['REMOTE_ADDR'])

        if self.client_ip is False:
            self.client_ip = http.VerifyIP(self.request.META.get(
                'HTTP_X_REAL_IP', ''))

        if self.client_ip is False:
            self.client_ip = http.VerifyIP(self.request.META.get(
                'HTTP_X_FORWARDED_FOR', '').split(',')[-1])

        if self.client_ip is False:
            self.client_ip = '0.0.0.0'

        self.scheme = self.request.META.get(
            'HTTP_X_SCHEME', '').strip() or self.request.scheme

        if self.scheme not in ('http', 'https'):
            self.scheme = 'http'

        return super(BaseView, self).dispatch(*args, **kwargs)
