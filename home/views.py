#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.views.generic import View
from django.http import HttpResponse

from core.view import BaseView as Base
from user.libs.online import count_online_users


class HomeView(Base, View):
    def get(self, request, *args, **kwargs):
        online_users = count_online_users()
        return HttpResponse(online_users)
