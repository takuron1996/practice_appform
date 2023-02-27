"""依存関係定義用のモジュール"""
import boto3
import injector


class SnsDependencies:
    def __init__(self):
        self.sns_resource = boto3.resource("sns", region_name="ap-northeast-1")


injector_instance = injector.Injector()
injector_instance.binder.bind(SnsDependencies, SnsDependencies().sns_resource)
