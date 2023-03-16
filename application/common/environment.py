"""環境変数定義用のモジュール"""

from pydantic import BaseSettings


class VariableSettings(BaseSettings):
    """環境変数を取得する設定クラス"""

    SECRET_KEY: str
    DJANGO_ALLOWED_HOSTS: str
    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    AWS_RESION_NAME: str = "ap-northeast-1"
    AWS_ENDPOINT_URL: str = "http://localstack:4566"
