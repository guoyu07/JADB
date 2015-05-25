#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.views.generic import View

from core.view import BaseView as Base


class AuthView(Base, View):
    # login page
    def get(self, request, *args, **kwargs):
        pass

    # login
    def post(self, request, *args, **kwargs):
        s_captcha = request.session.get('captcha', None)
        c_captcha = request.POST.get('captcha')

        if not s_captcha or not c_captcha or s_captcha.lower() != c_captcha.lower():
            if s_captcha is not None:
                del request.session['captcha']

            return super(Base, self).json_response(1, 'Captcha is invalid.')

        return super(Base, self).json_response()

    # logout
    def delete(self, request, *args, **kwargs):
        pass
