#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

import sys
from django.apps import AppConfig

from django.db.backends.mysql.base import DatabaseWrapper
from django.db.migrations.recorder import MigrationRecorder

from core import Core
from core.install import Install


class Initialize(Core, AppConfig):
    name = 'core'

    def ready(self):
        DatabaseWrapper._data_types['AutoField'] = \
            'integer UNSIGNED AUTO_INCREMENT'

        MigrationRecorder.Migration._meta.db_table = \
            self.get_table(MigrationRecorder.Migration._meta.db_table)

        install = Install()

        if self.installation_status == -2:
            install.install_database()
