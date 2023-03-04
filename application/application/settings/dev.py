"""DEV環境用の設定"""

from crm.injectors import DevModule, injector

from .base import *

DEBUG = True

injector.binder.install(DevModule())
