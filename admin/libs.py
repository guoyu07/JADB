#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core import Core
from admin.models import Admin


def insert_options(options):
    for name, value in options.items():
        Admin.objects.get_or_create(name=name, defaults={
            'value': value,
        })

        Core.options['name'] = value


def update_options(options):
    for name, value in options.items():
        Admin.objects.update_or_create(name=name, defaults={
            'value': value,
        })

        Core.options['name'] = value


def load_options():
    options = {}

    for option in Admin.objects.all():
        options[option.name] = option.value

    Core.options = options
