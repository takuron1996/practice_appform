"""STG環境用の設定"""
from crm.injectors import StgModule, injector

from .base import *

DEBUG = False
ROOT_URLCONF = "application.urls.base"
injector.binder.install(StgModule())
