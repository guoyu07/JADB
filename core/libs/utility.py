#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-


def version_count_equaled(shorter_version, longer_count):
    shorter_count = len(shorter_version)

    for x in xrange(longer_count):
        if x > shorter_count:
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

    for x in xrange(len(version1)):
        try:
            version1[x] = int(version1[x])
            version2[x] = int(version2[x])
        except ValueError:
            return False

        if version1[x] > version2[x]:
            return 1
        elif version1[x] < version2[x]:
            return -1

    return 0
