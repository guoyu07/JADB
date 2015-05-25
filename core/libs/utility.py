#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-


def version_count_equaled(shorter_version, longer_count):
    shorter_count = len(shorter_version)

    for i in xrange(longer_count):
        if i > shorter_count:
            shorter_version.append('0')

    return shorter_version


def version_compare(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')

    count1 = len(version1)
    count2 = len(version2)

    if count1 != count2:
        if count1 > count2:
            version2 = version_count_equaled(version2, count1)
        else:
            version1 = version_count_equaled(version1, count2)

    for i in xrange(len(version1)):
        try:
            version1[i] = int(version1[i])
            version2[i] = int(version2[i])
        except ValueError:
            return False

        if version1[i] > version2[i]:
            return 1
        elif version1[i] < version2[i]:
            return -1

    return 0


def random_char(length=4):
    import string
    try:
        from random import SystemRandom

        random = SystemRandom()
    except ImportError:
        import random

    return ''.join(random.choice(string.ascii_letters + string.digits) for i in xrange(length))
