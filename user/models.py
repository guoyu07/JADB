#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from core.libs import http
from django.conf import settings
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, unique=True)
    salt = models.CharField(max_length=16, unique=True)
    alias = models.CharField(
        blank=True, db_index=True,
        max_length=128, unique=True)
    email = models.EmailField(max_length=128, unique=True)
    gender = models.PositiveSmallIntegerField(default=3)
    url = models.URLField(max_length=255, blank=True)
    role = models.PositiveSmallIntegerField(default=3)
    reg_time = models.DateTimeField(auto_now_add=True, db_index=True)
    reg_ip = models.GenericIPAddressField(
        db_index=True, default=http.FetchClientIP())
    log_time = models.DateTimeField(db_index=True)
    log_ip = models.GenericIPAddressField(
        db_index=True, default=http.FetchClientIP())

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + 'user'
