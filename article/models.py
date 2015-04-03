#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from datetime import datetime
from django.conf import settings
from django.db import models


class Article(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)
    title = models.CharField(db_index=True, max_length=255)
    category_id = models.PositiveIntegerField(db_index=True)
    created_time = models.DateTimeField(db_index=True, auto_now_add=True)
    modified_time = models.DateTimeField(db_index=True)
    content = models.TextField()
    draft = models.PositiveSmallIntegerField(default=0)
    views = models.PositiveIntegerField(db_index=True)

    def save(self, *args, **kwargs):
        self.modified_time = datetime.today()
        return super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = settings.DB_TABLE_PREFIX + 'article'
