#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.apps import AppConfig

from core import Core
from core.install import Install


class Initialize(AppConfig, Core):
    name = 'admin'

    def ready(self):
        install = Install()

        if self.installation_status == -1:
            install.install_options()
