#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from django.db import models
from django.conf import settings


class Commit(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)
    created_time = models.DateTimeField(db_index=True, auto_now_add=True)
    content = models.TextField()

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + 'commit'
