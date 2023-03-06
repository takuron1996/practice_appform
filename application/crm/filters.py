"""Djangoのfiltersの定義用モジュール"""

import django_filters

from crm.models import User


class UserFilter(django_filters.FilterSet):
    """ユーザ用のフィルター"""

    name = django_filters.CharFilter(field_name="name", lookup_expr="contains")
    """名前"""

    employee_number = django_filters.CharFilter(
        field_name="employee_number", lookup_expr="contains"
    )
    """社員番号"""

    class Meta:
        model = User
