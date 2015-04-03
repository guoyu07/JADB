#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jadb.models.settings")

application = get_wsgi_application()
