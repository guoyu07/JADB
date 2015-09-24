#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: jat@sinosky.org -*-

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

from core.form import BaseForm as Base
from user.models import User
from user.libs.info import get_user


class LoginForm(Base):
    captcha = Base.forms.CharField(max_length=4)

    def __init__(self, request, *args, **kwargs):
        self.captcha = request.session.get('captcha')

        super(LoginForm, self).__init__(request.POST, *args, **kwargs)

        self.fields['name'].error_messages['required'] = 'Please input your user name or e-mail address.'
        self.fields['password'].error_messages['required'] = 'Please input your password.'
        self.fields['captcha'].error_messages['required'] = 'Please input the captcha.'

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        if 'captcha' in cleaned_data:
            if self.captcha and self.captcha.lower() == cleaned_data['captcha'].lower():
                if 'name' in cleaned_data and 'password' in cleaned_data:
                    try:
                        validate_email(cleaned_data['name'])
                    except ValidationError:
                        cleaned_data['type'] = 'name'
                    else:
                        cleaned_data['type'] = 'email'

                    user = get_user(cleaned_data['name'], type=cleaned_data['type'])
                    if user:
                        if check_password(cleaned_data['password'], user['password']):
                            self.user = user
                        else:
                            self.add_error('password', ValidationError('Password is invalid.', code='invalid'))
                    else:
                        self.add_error('name', ValidationError('No account found.', code='not_exist'))
            else:
                self.add_error('captcha', ValidationError('Captcha is invalid.', code='invalid'))

        return cleaned_data

    class Meta:
        model = User
        fields = ['name', 'password']
