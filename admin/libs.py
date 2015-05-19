#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core.lib import BaseLib as Base
from admin.models import Admin


class Option(Base):
    def insert_options(self, options):
        for name, value in options.items():
            Admin.objects.get_or_create(name=name, defaults={
                'value': value
            })

            Base.Core.options['name'] = value

    def update_options(self, options):
        for name, value in options.items():
            Admin.objects.update_or_create(name=name, defaults={
                'value': value
            })

            Base.Core.options['name'] = value

    def load_options(self):
        options = {}

        for option in Admin.objects.all():
            options[option.name] = option.value

        Base.Core.options = options
