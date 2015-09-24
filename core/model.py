#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.db import models

from core import Core


class BaseModel(Core, models.Model):
    models = models
    Core = Core

    class Meta:
        abstract = True
