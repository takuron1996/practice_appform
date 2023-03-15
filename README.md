# template_django

# 準備
- .envの生成

## env
```env
# POSTGRES_NAME="任意のデータベース名"
# POSTGRES_USER="任意のユーザ名"
# POSTGRES_PASSWORD="任意のパスワード"
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
# SECRET_KEYは任意
SECRET_KEY="postgres"
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# AWS
# SMS用のIAMロール
AWS_ACCESS_KEY_ID="localstack"
AWS_SECRET_ACCESS_KEY="localstack"

## 環境を指定（ローカル環境）
DJANGO_SETTINGS_MODULE=application.settings.local
```
