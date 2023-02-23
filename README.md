# template_django

# 準備
- .envの生成
- .env.prodの生成
- data/db の生成
- staticの生成

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
# 開発環境のためTrue
DEBUG=1
```

## env.prod
```env.prod
# POSTGRES_NAME="任意のデータベース名"
# POSTGRES_USER="任意のユーザ名"
# POSTGRES_PASSWORD="任意のパスワード"
POSTGRES_NAME=postgres
POSTGRES_USER=postgres-prod
POSTGRES_PASSWORD=postgres-prod
# SECRET_KEYは任意
SECRET_KEY="postgres"
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
# 本番環境のためTrue
DEBUG=0
```