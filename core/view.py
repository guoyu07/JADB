#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.http import HttpResponseBadRequest, JsonResponse
from django.utils.timezone import now
from django.utils.translation import ugettext as _

from core import Core
from core.libs.http import verify_ip
from user.libs.online import mark_online


class BaseView(Core):
    Core = Core

    def dispatch(self, request, *args, **kwargs):
        request.client_ip = verify_ip(request.META['REMOTE_ADDR']) or verify_ip(request.META.get('HTTP_X_REAL_IP')) \
            or verify_ip(request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[-1], True)

        request.user_agent = request.META.get('HTTP_USER_AGENT', '').strip()

        if not request.client_ip or not request.user_agent:
            return HttpResponseBadRequest()

        if request.session.session_key is not None and request.session.exists(request.session.session_key):
            ip = request.session.get('ip', None)
            ua = request.session.get('ua', None)

            if ip != request.client_ip or ua != request.user_agent:
                # clean cached session items
                request.session.clear()
                # delete session from database
                request.session.delete()
                # create a new empty session
                request.session.create()

                request.session['ip'] = request.client_ip
                request.session['ua'] = request.user_agent
        else:
            request.session['ip'] = request.client_ip
            request.session['ua'] = request.user_agent

        request.session['last_activity'] = now()
        mark_online(request.session.session_key)

        return super(BaseView, self).dispatch(request, *args, **kwargs)

    """
    Normally, err_num is a negative number if something goes wrong.
    err_num is equal to zero when everything is correct and nothing to respond.
    err_num is a positive number if api needs front-end to handle the response.

    msg and uri can not be set up together.
    """
    def json_response(self, err_num=0, msg='', uri=''):
        if msg:
            msg = _(msg)

        if uri:
            uri = self.request.build_absolute_uri(uri)

        return JsonResponse({
            'err_num': err_num,
            'msg': msg,
            'uri': uri
        })
