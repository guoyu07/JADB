#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    parent_id = models.PositiveIntegerField(
        db_index=True, max_length=5, default=0)
    alias = models.CharField(db_index=True, max_length=128)

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + 'category'
