#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.http import HttpResponseBadRequest, JsonResponse
from django.utils.timezone import now
from django.utils.translation import ugettext as _, get_language
from django.shortcuts import render_to_response

from core import Core
from core.libs.http import verify_ip
from user.libs.online import mark_online
#from user.libs.info import get_user


class BaseView(Core):
    Core = Core

    def dispatch(self, request, *args, **kwargs):
        request.now = now()

        request.client_ip = verify_ip(request.META['REMOTE_ADDR']) or verify_ip(request.META.get('HTTP_X_REAL_IP')) \
            or verify_ip(request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[-1], True)
        request.user_agent = request.META.get('HTTP_USER_AGENT', '').strip()

        if not request.client_ip or not request.user_agent:
            return HttpResponseBadRequest()

        clean_session = True

        if request.session.session_key is not None and request.session.exists(request.session.session_key):
            ip = request.session.get('ip')
            ua = request.session.get('ua')

            if ip == request.client_ip and ua == request.user_agent:
                last_activity = request.session.get('last_activity')
                user_id = request.session.get('user_id')
                remembered = request.session.get('remembered')

                # Clean session if not remembered user status and last activity time is before 1 day.
                if not user_id or remembered is True or (request.now - last_activity).days == 0:
                    clean_session = False

        if clean_session is True:
            # clean cached session items
            request.session.clear()
            # delete session from database
            request.session.delete()
            # create a new empty session
            request.session.create()

            request.session['ip'] = request.client_ip
            request.session['ua'] = request.user_agent

        request.session['last_activity'] = request.now
        mark_online(request.session.session_key)

        #request.user = get_user()

        return super(BaseView, self).dispatch(request, *args, **kwargs)

    """
    Normally, err_num is a negative number if something goes wrong.
    err_num is equal to zero when everything is correct and nothing to respond.
    err_num is a positive number if api needs front-end to handle the response.

    msg and uri should not be set up together.
    """
    def json_response(self, err_num=0, msg='', uri=''):

        if msg:
            if err_num == -1:
                msg = _(msg)
            elif err_num == -2:
                msg = {f: [_(e) for e in l] for f, l in msg.items()}

        if uri:
            uri = self.request.build_absolute_uri(uri)

        return JsonResponse({
            'err_num': err_num,
            'msg': msg,
            'uri': uri,
        })

    def get_redirect_uri(self):
        redirect = self.request.POST.get('redirect')

        # A redirect uri should not be a external link.
        if not redirect or redirect[0:4] == 'http' or redirect[0:2] == '//':
            redirect = ''

        return redirect

    def render_to_response(self, *args, **kwargs):
        # The default context.
        context = {
            'site_options': self.options,
            'language_code': get_language().split('-')[0] or 'en',
        }

        if 'context' in kwargs:
            context.update(kwargs['context'])

            kwargs['context'] = context
        elif len(args) >= 2:
            context.update(**args[1])

            args = list(args)
            args[1] = context
        else:
            kwargs['context'] = context

        return render_to_response(*args, **kwargs)
