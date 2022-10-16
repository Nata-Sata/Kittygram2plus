from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'retrieve':
            return request.method in SAFE_METHODS
        else:
            return (request.method in SAFE_METHODS
                    or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
