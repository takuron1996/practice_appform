"""DEV環境用の設定"""
from logging.config import dictConfig

from common.conf import ConfFile
from crm.injectors import DevModule, injector

from .base import *

DEBUG = False
ROOT_URLCONF = "application.urls.base"
injector.binder.install(DevModule())

# ログ設定
output_path = Path("output")
if not output_path.exists():
    output_path.mkdir()
dictConfig(ConfFile.get()["dev"]["logging"])
