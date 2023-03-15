"""Djangoのfiltersの定義用モジュール"""

from django_filters import DateTimeFilter, FilterSet

from crm.models import Customer


class CustomerFilter(FilterSet):
    """顧客情報のフィルタ"""

    created_at_min = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    """生成時刻の下限"""
    created_at_max = DateTimeFilter(field_name="created_at", lookup_expr="lte")
    """生成時刻の上限"""

    class Meta:
        model = Customer
        fields = [
            "name",
            "birth_of_date",
            "phone_number",
            "created_at_min",
            "created_at_max",
        ]
