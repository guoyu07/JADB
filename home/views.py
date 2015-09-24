#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.views.generic import View

from core.view import BaseView as Base
from user.libs.online import count_online_users


class HomeView(Base, View):
    def get(self, request, *args, **kwargs):
        return self.render_to_response('home.html', {
            'show_extended_title': False,
            'online_users': count_online_users(),
        })
