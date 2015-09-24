#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

import sys
import os

from django.core.wsgi import get_wsgi_application


sys.dont_write_bytecode = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('JADB_VERSION', '0.0.1 alpha')

application = get_wsgi_application()
