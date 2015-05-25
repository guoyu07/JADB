#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-


def verify_ip(ip, allow_private_addr=False):
    from IPy import IP

    if not ip:
        return False

    try:
        ip = IP(ip)
    except ValueError:
        return False

    if allow_private_addr is False and ip.iptype() != 'PUBLIC':
        return False

    return str(ip)
