#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

import pickle

from core.model import BaseModel as Base


class Admin(Base):
    name = Base.models.CharField(db_index=True, max_length=255)
    value = Base.models.TextField()

    def save(self, *args, **kwargs):
        self.value = pickle.dumps(self.value)
        return super(Admin, self).save(*args, **kwargs)

    def get(self, *args, **kwargs):
        self.value = pickle.loads(self.value)
        return super(Admin, self).get(*args, **kwargs)

    class Meta(Base.Meta):
        db_table = Base.settings.DB_TABLE_PREFIX + 'options'
