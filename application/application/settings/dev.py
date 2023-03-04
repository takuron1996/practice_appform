"""DEV環境用の設定"""

from .base import *
from crm.injectors import injector, DevModule

DEBUG = True

injector.binder.install(DevModule())
