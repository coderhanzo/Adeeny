# Extending default Permissions
from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_superadmin", False) or getattr(user, "is_imam", False)


class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_superadmin", False)


class IsImam(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_imam", False)


class IsAssociate(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user:
            return False
        return getattr(user, "is_associate", False)
