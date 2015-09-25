#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from picklefield.fields import PickledObjectField

from core.model import BaseModel as Base


class Admin(Base):
    name = Base.models.CharField(db_index=True, max_length=255)
    value = PickledObjectField()

    class Meta:
        db_table = Base.settings.DB_TABLE_PREFIX + 'options'
