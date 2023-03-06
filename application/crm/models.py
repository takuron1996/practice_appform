import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    """システムユーザ"""

    class Role(models.IntegerChoices):
        """ロールの種類"""

        GENERAL = 1
        """一般"""
        AUTHORIZER = 2
        """承認者"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    name = models.CharField(max_length=255)
    """氏名"""
    password = models.CharField(max_length=255)
    """パスワード"""
    email = models.CharField(max_length=255)
    """メールアドレス"""
    role = models.PositiveIntegerField(
        choices=Role.choices, default=Role.GENERAL
    )
    """ロール"""
    verified = models.BooleanField(default=False)
    """検証情報"""

    first_name = None
    last_name = None
    date_joined = None
    groups = None
    username = None
    is_active = None
    is_staff = None
    is_superuser = None

    USERNAME_FIELD = "employee_number"
    """認証に使用されるユーザー名のフィールドを指定"""

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.employee_number
