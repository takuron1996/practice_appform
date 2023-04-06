"""モデル用のモジュール"""
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator
from django.db import models
from django_ulid.models import ulid

from crm.managers import UserManager


class User(AbstractUser):
    """システムユーザ"""

    objects = UserManager()
    """Userモデルクラスとシステム利用者を作成する為のクラスを紐付ける"""

    id = models.CharField(
        max_length=26, primary_key=True, default=ulid.new, editable=False
    )
    """主キー"""
    employee_number = models.CharField(
        error_messages={"unique": "その社員番号のユーザーはすでに登録されています。"},
        help_text="半角英数字8文字の社員番号を入力してください。",
        max_length=8,
        unique=True,
        validators=[RegexValidator(r"^[0-9]{8}$", "8桁の数字を入力してください。")],
        verbose_name="社員番号",
    )
    """社員番号"""
    name = models.CharField(max_length=255, verbose_name="氏名")
    """氏名"""
    password = models.CharField(max_length=255, verbose_name="パスワード")
    """パスワード"""
    groups = models.ForeignKey(
        Group, on_delete=models.DO_NOTHING, related_name="users"
    )
    """システム利用者権限テーブル外部キー"""
    verified = models.BooleanField(default=False, verbose_name="検証情報")
    """検証情報"""

    first_name = None
    last_name = None
    date_joined = None
    username = None
    email = None

    USERNAME_FIELD = "employee_number"
    """認証に使用されるユーザー名のフィールドを指定"""

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.employee_number


class Customer(models.Model):
    """顧客情報"""

    phone_regex = RegexValidator(
        regex=r"^\d+$",
        message="電話番号の形式は0123456789",
    )
    """電話番号(日本)のバリデータ"""

    id = models.CharField(
        max_length=26, primary_key=True, default=ulid.new, editable=False
    )
    """主キー"""
    name = models.CharField(max_length=255, verbose_name="氏名")
    """氏名"""
    birth_of_date = models.DateField(verbose_name="生年月日")
    """生年月日"""
    phone_number = models.CharField(
        max_length=11, validators=[phone_regex], verbose_name="電話番号"
    )
    """電話番号"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="生成時刻")
    """生成時刻"""

    class Meta:
        db_table = "customer"
