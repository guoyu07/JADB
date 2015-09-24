#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.apps import AppConfig

from core import Core
from core.libs.install import install_options


class Initialize(Core, AppConfig):
    name = 'admin'

    def ready(self):
        from admin.libs import load_options

        if self.installation_status == -1:
            install_options()
            Core.installation_status = 0

        load_options()
