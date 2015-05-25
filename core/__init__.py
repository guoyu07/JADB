#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

import os

from django.conf import settings


default_app_config = 'core.init.Initialize'


class Core(object):
    settings = settings
    options = {}
    installation_status = None
    need_update = False
    version = os.environ['JADB_VERSION'].split(' ')
