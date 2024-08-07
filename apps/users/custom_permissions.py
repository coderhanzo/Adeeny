from rest_framework import permissions
from .models import User

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [User.Role.ADMIN, User.Role.IMAM]


class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.SUPERADMIN


class IsImam(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.IMAM


class IsAssociate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == User.Role.ASSOCIATE