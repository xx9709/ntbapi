from rest_framework.permissions import BasePermission
from user.models import UserRoleChoice

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_role == UserRoleChoice.ADMIN

class MasterPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_role == UserRoleChoice.MASTER

class ProrabPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_role == UserRoleChoice.PRORAB

class UchastnikPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.user_role == UserRoleChoice.UCHASNIK

