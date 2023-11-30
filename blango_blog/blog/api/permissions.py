from rest_framework import permissions

class IsAuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS

class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)