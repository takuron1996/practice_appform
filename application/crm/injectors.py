"""DI定義用のモジュール"""
import boto3
from injector import Binder, Injector, Module

from common.sms import SnsResource, SnsWrapper


class SnsWrapperModule(Module):
    def configure(self, binder):
        binder.bind(SnsWrapper)


class DevModule(Module):
    """DEV環境用のモジュール"""

    def configure(self, binder: Binder) -> None:
        sns_resource = SnsResource(
            boto3.resource(
                "sns",
                region_name="ap-northeast-1",
                endpoint_url="http://localstack:4566",
            )
        )
        binder.bind(SnsResource, to=sns_resource)


class StgModule(Module):
    """STG環境用のモジュール"""

    def configure(self, binder: Binder) -> None:
        sns_resource = SnsResource(
            boto3.resource("sns", region_name="ap-northeast-1")
        )
        binder.bind(SnsResource, to=sns_resource)


injector = Injector([SnsWrapperModule()])
