#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

import json
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    f = open(os.path.join(os.path.dirname(BASE_DIR), 'config.json'))
except IOError, e:
    sys.exit('Open configuration file error: %s' % e)
else:
    user_settings = json.loads(f.read())
    f.close()

SECRET_KEY = user_settings.get('secret_key', '')

DEBUG = user_settings.get('debug', False)

TEMPLATE_DEBUG = user_settings.get('debug', False)

INSTALLED_APPS = (
    'core',
    'admin',
    'user',
    'article',
    'comment',
    'category',
    'tag'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'wsgi.application'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_SCHEME', 'https')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': user_settings.get('db_user', 'root'),
        'PASSWORD': user_settings.get('db_password', 'root'),
        'HOST': user_settings.get('db_host', '127.0.0.1'),
        'PORT': user_settings.get('db_port', '3306'),
        'OPTIONS': {
            'init_command': '''SET NAMES "utf8" COLLATE "utf8_general_ci";
                            SET default_storage_engine={0};

                            CREATE DATABASE IF NOT EXISTS `{1}`
                            DEFAULT CHARACTER SET = "utf8"
                            DEFAULT COLLATE = "utf8_general_ci";

                            USE `{1}`;'''.format(
                                user_settings.get('db_engine', 'InnoDB'),
                                user_settings.get('db_name', 'jadb')
                            )
        }
    }
}

DB_TABLE_PREFIX = user_settings.get('db_table_prefix', 'jadb_')

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')

ALLOWED_CHARACTERS = '[a-zA-Z0-9_@\+\.-]+'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '%s' % user_settings.get(
            'redis_location', 'redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SESSION_COOKIE_AGE = user_settings.get('session_cookie_age', 2419200)
SESSION_COOKIE_DOMAIN = user_settings.get('session_cookie_domain', None)
SESSION_COOKIE_HTTPONLY = user_settings.get('session_cookie_httponly', True)
SESSION_COOKIE_NAME = user_settings.get(
    'session_cookie_name', 'jadb_sessionid')
SESSION_COOKIE_PATH = user_settings.get('session_cookie_path', '/')
SESSION_COOKIE_SECURE = user_settings.get('session_cookie_secure', True)
