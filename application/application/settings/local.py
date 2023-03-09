"""LOCAL環境用の設定"""

from crm.injectors import DevModule, injector

from .base import *

DEBUG = True

REST_FRAMEWORK.update(
    {"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"}
)

SPECTACULAR_SETTINGS = {
    "TITLE": "プロジェクト名",
    "DESCRIPTION": "詳細",
    "VERSION": "1.0.0",
    # オプション
    # 'SERVE_INCLUDE_SCHEMA': False,
}

INSTALLED_APPS += ["drf_spectacular"]

ROOT_URLCONF = "application.urls.local"

injector.binder.install(DevModule())

# ログ設定
output_path = Path("output")
if not output_path.exists():
    output_path.mkdir()
dictConfig(ConfFile.get()["local"]["logging"])
