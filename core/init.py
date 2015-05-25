#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.apps import AppConfig
from django.db.backends.mysql.base import DatabaseWrapper
from django.db.migrations.recorder import MigrationRecorder

from core import Core
from core.libs.install import get_installation_status, install_database


class Initialize(Core, AppConfig):
    name = 'core'

    def ready(self):
        DatabaseWrapper._data_types['AutoField'] = 'integer UNSIGNED AUTO_INCREMENT'

        MigrationRecorder.Migration._meta.db_table = self.settings.DB_TABLE_PREFIX + MigrationRecorder.Migration._meta.db_table

        Core.installation_status = get_installation_status()
        if self.installation_status == -2:
            install_database()
            Core.installation_status = -1
