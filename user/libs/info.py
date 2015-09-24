#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.core.cache import cache
from django_redis import get_redis_connection
from django.core.exceptions import ObjectDoesNotExist

from user.models import User


_key = ':jadb:users.info.%s:%s'


def get_user(id, type='id', timeout=60*10):
    # For security.
    if type not in ('id', 'name', 'email'):
        return False

    key = _key % (type, id)
    user = cache.get(key)

    if user:
        if type != 'id':
            user = get_user(user, 'id', timeout)

        if timeout and cache.ttl(key) < timeout:
            con = get_redis_connection()
            con.expire(key, timeout)
    else:
        # A trick for realize http://php.net/manual/en/language.variables.variable.php
        kwargs = {}
        kwargs[type] = type
        try:
            user = User.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None
        else:
            user = user.__dict__

        if timeout:
            if type == 'id':
                cache.set(key, user, timeout=timeout)
            else:
                cache.set(_key % ('id', user['id']), user, timeout=timeout)
                cache.set(key, user['id'], timeout=timeout)

    return user


def create_user(info, is_admin=False):
    _info = {
        'name': info['name'],
        'email': info['email'],
        'reg_salt': info['reg_salt'],
        'password': info['password']
    }

    if is_admin:
        _info.update({
            'role': info['role'] if info['role'] in ('1', '2') else '3'
        })

        if not _info['password']:
            from core.libs.utility import random_char
            #from core.libs.email import send_activate_email

            password = random_char(12, True)
            _info['password'] = encrypt_password(password, _info['reg_salt'])
            #send_activate_email(_info['email'], _info['name'], password)

    user = User(**_info)
    user.save()
    return user.id


def update_userinfo(id, info, is_admin=False):
    _info = {
        'gender': info['gender'] if info['gender'] in ('1', '2') else '3',
        'url': info['url']
    }

    if is_admin is True:
        _info.update({
            'email': info['email'],
            'name': info['name'],
            'role': info['role'] if info['role'] in ('1', '2') else '3'
        })

        if info['password'] and info['reg_salt']:
            _info.update({
                'password': info['password'],
                'reg_salt': info['reg_salt']
            })

    remove_cache(id)
    return User.objects.filter(id=id).update(**info)


def delete_user(id):
    remove_cache(id)
    return User.objects.filter(id=id).delete()


def remove_cache(id):
    key = _key % ('id', id)
    user = cache.get(key)

    if user:
        cache.delete(_key % ('name', user['name']))
        cache.delete(_key % ('email', user['email']))
        cache.delete(key)


def encrypt_password(password, salt):
    import hashlib
    from django.contrib.auth.hashers import make_password

    l = len(salt) // 2

    make_password(hashlib.sha1(salt[0:l] + password + salt[l:]).hexdigest())
