# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# The secret key and recaptcha public key is automatically generated when the
# project is created
SECRET_KEY = '{{ cookiecutter.secret_key }}'
RECAPTCHA_PUBLIC_KEY = '{{ cookiecutter.recaptcha_public_key }}'

WTF_CSRF_ENABLED = True
PROPAGATE_EXCEPTIONS = True
