"""STG環境用の設定"""
from .base import *
from crm.injectors import injector, StgModule

DEBUG = False

injector.binder.injector(StgModule())