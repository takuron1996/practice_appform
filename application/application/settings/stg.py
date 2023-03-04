"""STG環境用の設定"""
from crm.injectors import StgModule, injector

from .base import *

DEBUG = False

injector.binder.injector(StgModule())
