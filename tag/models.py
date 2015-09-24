#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core.model import BaseModel as Base


class Tag(Base):
    title = Base.models.CharField(db_index=True, max_length=255)
    alias = Base.models.CharField(db_index=True, max_length=128)

    class Meta:
        db_table = Base.Core.settings.DB_TABLE_PREFIX + 'tag'
