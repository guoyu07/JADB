#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

import sys
import os

from django.core.management import execute_from_command_line


sys.dont_write_bytecode = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('JADB_VERSION', '0.0.1 alpha')

execute_from_command_line(sys.argv)
