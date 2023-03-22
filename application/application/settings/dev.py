"""DEV環境用の設定"""
from logging.config import dictConfig

from common.conf import ConfFile
from crm.injectors import DevModule, injector

from .base import *


injector.binder.install(DevModule())

# ログ設定
dictConfig(ConfFile.get()["dev"]["logging"])
