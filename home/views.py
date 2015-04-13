#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from django.http import HttpResponse

from core.views import BaseView


class HomeView(BaseView):
    def __init__(self):
        pass

    def dispatch(self, *args, **kwargs):
        super(HomeView, self).__init__()
        return super(HomeView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.client_ip)

    def post(self, request, *args, **kwargs):
        return HttpResponse(self.scheme)
