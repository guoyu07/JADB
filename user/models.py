#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core.model import BaseModel as Base
from core.libs import http


class User(Base):
    name = Base.models.CharField(max_length=128, unique=True)
    password = Base.models.CharField(max_length=128, unique=True)
    salt = Base.models.CharField(max_length=16, unique=True)
    alias = Base.models.CharField(
        blank=True, db_index=True, max_length=128, unique=True)
    email = Base.models.EmailField(max_length=128, unique=True)
    gender = Base.models.PositiveSmallIntegerField(default=3)
    url = Base.models.URLField(max_length=255, blank=True)
    role = Base.models.PositiveSmallIntegerField(default=3)
    reg_time = Base.models.DateTimeField(auto_now_add=True, db_index=True)
    reg_ip = Base.models.GenericIPAddressField(db_index=True)
    log_time = Base.models.DateTimeField(db_index=True)
    log_ip = Base.models.GenericIPAddressField(db_index=True)

    class Meta(Base.Meta):
        db_table = Base.Core.settings.DB_TABLE_PREFIX + 'user'
