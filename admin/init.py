#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.apps import AppConfig

from core import Core


class Initialize(Core, AppConfig):
    name = 'admin'

    def ready(self):
        from core.install import Install
        from admin.libs import Option

        install = Install()

        if self.installation_status == -1:
            install.install_options()

        Option().load_options()
