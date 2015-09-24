#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core.model import BaseModel as Base


class Category(Base):
    title = Base.models.CharField(db_index=True, max_length=255)
    parent_id = Base.models.PositiveIntegerField(db_index=True, default=0)
    alias = Base.models.CharField(db_index=True, max_length=128)

    class Meta:
        db_table = Base.Core.settings.DB_TABLE_PREFIX + 'category'
