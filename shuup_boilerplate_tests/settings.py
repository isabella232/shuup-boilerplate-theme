# -*- coding: utf-8 -*-
# This file is part of Shuup Boilerplate Theme.
#
# Copyright (c) 2012-2016, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import os
import tempfile

DEBUG = False
SECRET_KEY = "xxx"

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # shuup themes
    'shuup.themes.classic_gray',
    # shuup
    'shuup.addons',
    'shuup.admin',
    'shuup.core',
    'shuup.default_tax',
    'shuup.front',
    'shuup.front.apps.auth',
    'shuup.front.apps.customer_information',
    'shuup.front.apps.personal_order_history',
    'shuup.front.apps.saved_carts',
    'shuup.front.apps.registration',
    'shuup.front.apps.simple_order_notification',
    'shuup.front.apps.simple_search',
    'shuup.notify',
    'shuup.simple_cms',
    'shuup.customer_group_pricing',
    'shuup.campaigns',
    'shuup.simple_supplier',
    'shuup.order_printouts',
    'shuup.testing',
    'shuup.utils',
    'shuup.xtheme',
    'shuup.reports',
    'shuup.default_reports',
    # external apps
    'bootstrap3',
    'django_jinja',
    'easy_thumbnails',
    'filer',
    'registration',
    'rest_framework',
    'shuup_boilerplate_theme'
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'shuup.front.middleware.ProblemMiddleware',
    'shuup.front.middleware.ShuupFrontMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            tempfile.gettempdir(),
            'shuup_boilerplate_tests.sqlite3'
        ),
    }
}

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "var", "media")

STATIC_URL = "static/"

ROOT_URLCONF = 'shuup_workbench.urls'

LANGUAGES = [
    ('en', 'English'),
]

PARLER_DEFAULT_LANGUAGE_CODE = "en"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}
_TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
]
TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
            "environment": "shuup.xtheme.engine.XthemeEnvironment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "debug": DEBUG
        }
    },
]
