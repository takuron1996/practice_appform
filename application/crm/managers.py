from django.contrib.auth.models import BaseUserManager, Group

from crm.enums import UserRole


class UserManager(BaseUserManager):
    """システム利用者を作成する為のクラス"""

    use_in_migrations = True

    def create_user(
        self,
        employee_number: str,
        group: UserRole,
        password: str,
        **extra_fields
    ):
        """システムユーザーを作成

        Args:
            employee_number (str): 社員番号
            password (str): パスワード
            group (UserRole): ユーザー権限
        Returns:
            作成したシステムユーザー
        """

        # 初期バスワードは社員番号とする
        if password is None:
            password = employee_number

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        group, _ = Group.objects.get_or_create(name=group.value)

        user = self.model(
            employee_number=employee_number, groups=group, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
