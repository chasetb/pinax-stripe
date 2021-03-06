import os

import django

old = django.VERSION < (1, 8)

DEBUG = True
USE_TZ = True
TIME_ZONE = "UTC"
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("PINAX_STRIPE_DATABASE_ENGINE", "django.db.backends.sqlite3"),
        "HOST": os.environ.get("PINAX_STRIPE_DATABASE_HOST", "127.0.0.1"),
        "NAME": os.environ.get("PINAX_STRIPE_DATABASE_NAME", "pinax_stripe"),
        "USER": os.environ.get("PINAX_STRIPE_DATABASE_USER", ""),
    }
}
MIDDLEWARE = [  # from 2.0 onwards, only MIDDLEWARE is used
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]
MIDDLEWARE_CLASSES = MIDDLEWARE
ROOT_URLCONF = "pinax.stripe.tests.urls"
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "jsonfield",
    "pinax.stripe",
]
SITE_ID = 1
PINAX_STRIPE_PUBLIC_KEY = ""
PINAX_STRIPE_SECRET_KEY = ""
PINAX_STRIPE_SUBSCRIPTION_REQUIRED_EXCEPTION_URLS = ["pinax_stripe_subscription_create"]
PINAX_STRIPE_SUBSCRIPTION_REQUIRED_REDIRECT = "pinax_stripe_subscription_create"
PINAX_STRIPE_HOOKSET = "pinax.stripe.tests.hooks.TestHookSet"
TEMPLATE_DIRS = [
    "pinax/stripe/tests/templates"
]
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [
        "pinax/stripe/tests/templates"
    ],
    "APP_DIRS": True,
    "OPTIONS": {
        "debug": True,
        "context_processors": [
            "django.contrib.auth.context_processors.auth",
            "django.{}.context_processors.debug".format("core" if old else "template"),
            "django.{}.context_processors.i18n".format("core" if old else "template"),
            "django.{}.context_processors.media".format("core" if old else "template"),
            "django.{}.context_processors.static".format("core" if old else "template"),
            "django.{}.context_processors.tz".format("core" if old else "template"),
            "django.{}.context_processors.request".format("core" if old else "template")
        ],
    },
}]
SECRET_KEY = "pinax-stripe-secret-key"
