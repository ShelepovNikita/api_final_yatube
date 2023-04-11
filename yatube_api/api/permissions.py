from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Права на редактирование записей доступны только автору поста.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
