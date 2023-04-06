"""パーミッションモジュール"""

from logging import getLogger

from rest_framework.permissions import BasePermission

from common.constant import LoggerName
from crm.enums import UserRole

application_loogger = getLogger(LoggerName.APPLICATION.value)


class IsGeneral(BasePermission):
    """一般権限"""

    def has_permission(self, request, view):
        """権限チェック"""
        return request.user.groups.name == UserRole.GENERAL.value


class IsApprover(BasePermission):
    """承認者権限"""

    def has_permission(self, request, view):
        """権限チェック"""
        return request.user.groups.name == UserRole.APPROVER.value


class IsManagement(BasePermission):
    """管理者権限"""

    def has_permission(self, request, view):
        """権限チェック"""
        return request.user.groups.name == UserRole.MANAGEMENT.value


class IsAdmin(BasePermission):
    """admin権限"""

    def has_permission(self, request, view):
        """権限チェック"""
        return request.user.groups.name == UserRole.ADMIN.value
