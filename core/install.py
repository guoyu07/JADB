#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core import Core


class Install(Core):
    def __init__(self):
        if self.installation_status is None:
            Core.installation_status = self.get_installation_status()

    def get_installation_status(self):
        import pickle

        from django.db import connection

        from core.libs.utility import version_compare

        cursor = connection.cursor()

        try:
            cursor.execute(
                'SELECT value FROM %s WHERE name = "jadb_version"' %
                self.get_table('options'))
        except Exception, e:
            return -2

        version = cursor.fetchone()

        if version is None:
            return -2

        version = pickle.loads(version[0])

        if version_compare(version, self.version[0]) != 0:
            return -2

        return 0

    def install_database(self):
        from django.core.management import call_command

        call_command('migrate')

        Core.installation_status = -1

    def install_options(self):
        from admin.libs import Option

        option = Option()

        option.insert_options({
            'site_name': 'DAJB'
        })

        option.update_options({
            'jadb_version': self.version[0]
        })

        Core.installation_status = 0
