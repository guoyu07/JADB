#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.utils import timezone
from django_redis import get_redis_connection


now = timezone.now()
prefix = ':jadb:users.online:%02d%02d'
key = prefix % (now.hour, now.minute)

con = get_redis_connection()


def mark_online(sessionid):
    if not con.sismember(key, sessionid):
        con.sadd(key, sessionid)
        con.expire(key, 7200)


def count_online_users(minutes=5):
    hour = now.hour
    minute = now.minute

    keys = [key]

    for x in xrange(2, minutes):
        if minute == 0:
            if hour == 0:
                hour = 23
            else:
                hour -= 1

            minute = 59
        else:
            minute -= 1

        keys.append(prefix % (hour, minute))

    return len(con.sunion(*keys))
