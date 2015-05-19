#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from core.model import BaseModel as Base


class Commit(Base):
    user_id = Base.models.PositiveIntegerField(db_index=True)
    created_time = Base.models.DateTimeField(db_index=True, auto_now_add=True)
    content = Base.models.TextField()

    class Meta(Base.Meta):
        db_table = Base.Core.settings.DB_TABLE_PREFIX + 'commit'
