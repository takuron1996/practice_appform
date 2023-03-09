"""DEV環境用の設定"""
from crm.injectors import StgModule, injector

from .base import *

DEBUG = False
ROOT_URLCONF = "application.urls.base"
injector.binder.install(StgModule())

# ログ設定
output_path = Path("output")
if not output_path.exists():
    output_path.mkdir()
dictConfig(ConfFile.get()["dev"]["logging"])
