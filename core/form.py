#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django import forms

from core import Core


class BaseForm(Core, forms.ModelForm):
    forms = forms
    Core = Core
