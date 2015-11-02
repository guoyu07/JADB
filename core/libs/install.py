#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core import Core


def get_installation_status():
    from django.db import connection
    from picklefield.fields import dbsafe_decode

    from core.libs.utility import version_compare

    cursor = connection.cursor()

    try:
        cursor.execute('SELECT value FROM %soptions WHERE name = "jadb_version"' % Core.settings.DB_TABLE_PREFIX)
    except Exception:
        return -2

    version = cursor.fetchone()
    if version is None:
        return -2

    version = dbsafe_decode(version[0])
    if version_compare(version, Core.version[0]) != 0:
        return -2

    return 0


def install_database():
    from django.core.management import call_command

    call_command('migrate')


def install_options():
    from admin.libs import insert_options, update_options

    insert_options({
        'site_name': 'JADB',
        'site_description': 'Just Another Django Blog',
    })

    update_options({
        'jadb_version': Core.version[0],
    })
