"""テストのutilsモジュール"""


def login(client, login_authority):
    """ログイン処理

    Args:
        client(APIClient): API用のクライアント
        login_authority(dict): ログイン情報
    """
    client.login(**login_authority)
