#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from IPy import IP


def VerifyIP(ip):
    try:
        ip = IP(ip)
    except ValueError:
        return False

    if ip.iptype() != 'PUBLIC':
        return False

    return ip
