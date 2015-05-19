#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.utils import timezone

from core.model import BaseModel as Base


class Article(Base):
    user_id = Base.models.PositiveIntegerField(db_index=True)
    title = Base.models.CharField(db_index=True, max_length=255)
    created_time = Base.models.DateTimeField(db_index=True, auto_now_add=True)
    modified_time = Base.models.DateTimeField(db_index=True)
    content = Base.models.TextField()
    draft = Base.models.PositiveSmallIntegerField(db_index=True, default=0)
    views = Base.models.PositiveIntegerField(db_index=True, default=0)

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        return super(Article, self).save(*args, **kwargs)

    class Meta(Base.Meta):
        db_table = Base.Core.settings.DB_TABLE_PREFIX + 'article'
