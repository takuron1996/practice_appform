"""列挙型をまとめるモジュール"""
from enum import Enum


class UserRole(Enum):
    """ユーザー権限"""

    GENERAL = "一般"
    """一般権限"""
    APPROVER = "承認者"
    """承認者権限"""
    MANAGEMENT = "管理者"
    """管理職権限"""
    ADMIN = "admin"
    """admin権限"""
