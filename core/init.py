#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

import sys
from django.apps import AppConfig

from django.db.backends.mysql.base import DatabaseWrapper

from core import Core
from core.install import Install


class Initialize(AppConfig, Core):
    name = 'core'

    def ready(self):
        DatabaseWrapper._data_types['AutoField'] = \
            'integer UNSIGNED AUTO_INCREMENT'

        install = Install()

        if self.installation_status == -2:
            install.install_database()
