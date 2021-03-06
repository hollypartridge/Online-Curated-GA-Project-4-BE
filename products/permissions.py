from rest_framework import permissions

class isOwnerOrReadyOnly(permissions.BasePermission):

    def has_object_permission(self, request, _view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user