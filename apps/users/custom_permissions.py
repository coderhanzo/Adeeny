# Extending default Permissions
from rest_framework import Permissions


class IsAdminUser(Permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_superadmin", False) or getattr(user, "is_imam", False)


class IsSuperAdmin(Permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_superadmin", False)


class IsImam(Permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_imam", False)


class IsAssociate(Permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_associate", False)
