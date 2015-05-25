#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.http import HttpResponse
from django.views.generic import View

from core.view import BaseView as Base
from captcha.libs import generate_image
from core.libs.utility import random_char


class CaptchaView(Base, View):
    def get(self, request, *args, **kwargs):
        captcha = random_char()
        request.session['captcha'] = captcha
        out = generate_image(captcha)

        response = HttpResponse(content_type='image/jpeg')
        response.write(out.read())
        response['Content-length'] = out.tell()

        return response
