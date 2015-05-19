#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.http import HttpResponseBadRequest
from django.utils import timezone

from core import Core
from core.libs import http

from user.libs import mark_online


class BaseView(Core):
    Core = Core

    def dispatch(self, request, *args, **kwargs):
        request.client_ip = http.VerifyIP(request.META['REMOTE_ADDR']) or \
            http.VerifyIP(request.META.get('HTTP_X_REAL_IP', '')) or \
            http.VerifyIP(request.META.get(
                'HTTP_X_FORWARDED_FOR', '').split(',')[-1]) or \
            HttpResponseBadRequest()

        request.user_agent = request.META.get(
            'HTTP_USER_AGENT', '').strip() or HttpResponseBadRequest()

        sessionid = request.COOKIES.get(
            self.settings.SESSION_COOKIE_NAME, None)

        if sessionid is None or not request.session.exists(sessionid):
            request.session['ip'] = request.client_ip
            request.session['ua'] = request.user_agent
        else:
            ip = request.session.get('ip', None)
            ua = request.session.get('ua', None)

            if ip == request.client_ip and ua == request.user_agent:
                request.session['last_activity'] = timezone.now()
                mark_online(sessionid)
            else:
                request.session.flush()

        return super(BaseView, self).dispatch(request, *args, **kwargs)
