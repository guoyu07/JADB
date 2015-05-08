#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.db import models

from core import Core


class BaseModel(models.Model, Core):
    models = models
    Core = Core

    class Meta(object):
        abstract = True
