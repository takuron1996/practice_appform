"""DI定義用のモジュール"""
import boto3
from injector import Binder, Injector, Module

from common.environment import VariableSettings
from common.sms import SnsResource, SnsWrapper

settings = VariableSettings()
"""環境変数読み込み用のグローバル変数"""


class SnsWrapperModule(Module):
    def configure(self, binder):
        binder.bind(SnsWrapper)


class LocalModule(Module):
    """Local環境用のモジュール"""

    def configure(self, binder: Binder) -> None:
        sns_resource = SnsResource(
            boto3.resource(
                "sns",
                region_name=settings.AWS_RESION_NAME,
                endpoint_url=settings.AWS_ENDPOINT_URL,
            )
        )
        binder.bind(SnsResource, to=sns_resource)


class DevModule(Module):
    """Dev環境用のモジュール"""

    def configure(self, binder: Binder) -> None:
        sns_resource = SnsResource(
            boto3.resource("sns", region_name=settings.AWS_RESION_NAME)
        )
        binder.bind(SnsResource, to=sns_resource)


injector = Injector([SnsWrapperModule()])
