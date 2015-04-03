#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from article import libs
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_safe


@require_safe
def index(request):
    return HttpResponse(html)
