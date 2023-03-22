"""LOCAL環境用の設定"""

from logging.config import dictConfig

from common.conf import ConfFile
from crm.injectors import LocalModule, injector

from .base import *

REST_FRAMEWORK.update(
    {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}
)

SPECTACULAR_SETTINGS = {
    "TITLE": "プロジェクト名",
    "DESCRIPTION": "詳細",
    "VERSION": "1.0.0",
}

INSTALLED_APPS += ["drf_spectacular"]

ROOT_URLCONF = "application.urls.local"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

injector.binder.install(LocalModule())

# ログ設定
output_path = Path("output")
if not output_path.exists():
    output_path.mkdir()
dictConfig(ConfFile.get()["local"]["logging"])
