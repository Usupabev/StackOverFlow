from rest_framework.permissions import BasePermission


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj.author
