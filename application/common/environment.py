"""環境変数定義用のモジュール"""

from pydantic import BaseSettings


class DjangoSettings(BaseSettings):
    """Django絡みの環境変数を設定するクラス"""

    DEBUG: bool = False
    """デバッグモードの切り替え"""
    SECRET_KEY: str
    """Djangoのシークレットキー"""
    DJANGO_ALLOWED_HOSTS: str
    """リクエストを許可するホスト名"""
    POSTGRES_NAME: str
    """PostgreSQLのデータベース名"""
    POSTGRES_USER: str
    """PostgreSQLのユーザ名"""
    POSTGRES_PASSWORD: str
    """PostgreSQLのパスワード"""

class AwsSettings(BaseSettings):
    """AWS絡みの環境変数を設定するクラス"""
    RESION_NAME: str = "ap-northeast-1"
    """AWSのリージョン"""
    ENDPOINT_URL: str = "http://localstack:4566"
    """ローカルスタックコンテナのURL"""

django_settings = DjangoSettings()
"""Django用の環境変数"""

aws_settings = AwsSettings()
"""AWS用の環境変数"""