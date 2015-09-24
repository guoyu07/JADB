#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.views.generic import View
from django.core.cache import cache

from core.view import BaseView as Base
from account.forms.auth import LoginForm


class LoginView(Base, View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        key = ':jadb:login.ip:%s' % request.client_ip
        time = cache.get(key, 0)
        time += 1

        cache.set(key, time, timeout=60)

        if time > 10:
            return self.json_response(-1, 'You tried logining too many times. Have a rest and try again later.')

        form = LoginForm(request)

        if self.request.session.get('captcha') is not None:
            del self.request.session['captcha']

        if not form.is_valid():
            return self.json_response(-2, form.errors)

        if request.POST.get('remember'):
            request.session['remembered'] = True
        else:
            request.session['remembered'] = False
            request.session.set_expiry(0)

        request.session['user_id'] = form.user['id']

        return self.json_response(0, uri=self.get_redirect_uri())


class LogoutView(Base, View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        return self.json_response(0, uri=self.get_redirect_uri())


class RegisterView(Base, View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
