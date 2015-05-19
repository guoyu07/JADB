#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-


def VerifyIP(ip):
    from IPy import IP

    try:
        ip = IP(ip)
    except ValueError:
        return False

    if ip.iptype() != 'PUBLIC':
        return False

    return str(ip)
