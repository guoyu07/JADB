#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Jat -*-

from django.db.backends.mysql.base import DatabaseWrapper
from os import path
import json
import sys

BASE_DIR = path.dirname(path.abspath(__file__))

try:
    f = open(path.join(path.dirname(BASE_DIR), 'config.json'))
except IOError, e:
    sys.exit('Open configuration file error: %s' % e)
else:
    user_settings = json.loads(f.read())
    f.close()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = user_settings.get('secret_key', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'article',
    'category',
    'comment',
    'tag',
    'user'
)

MIDDLEWARE_CLASSES = (

)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': user_settings.get('db_engine', 'django.db.backends.mysql'),
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
                                user_settings.get('db_engine', 'INNODB'),
                                user_settings.get('db_name', 'jadb')
                            )
        }
    }
}

DB_TABLE_PREFIX = user_settings.get('db_table_prefix', 'jadb_')

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = path.join(BASE_DIR, 'static')

DatabaseWrapper._data_types['AutoField'] = 'integer UNSIGNED AUTO_INCREMENT'
