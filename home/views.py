#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.http import HttpResponse

from core.view import BaseView as Base


class HomeView(Base):
    def get(self, *args, **kwargs):
        return HttpResponse(self.client_ip)

    def post(self, *args, **kwargs):
        return HttpResponse(self.scheme)
