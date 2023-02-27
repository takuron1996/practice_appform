"""DI定義用のモジュール"""
from injector import Injector, Module

from common.sms import SnsResource, SnsWrapper


class SnsWrapperModule(Module):
    def configure(self, binder):
        binder.bind(SnsWrapper)


class SnsResourceModule(Module):
    def configure(self, binder):
        binder.bind(SnsResource, to=SnsResource().sns_resource)


injector = Injector([SnsWrapperModule(), SnsResourceModule()])
