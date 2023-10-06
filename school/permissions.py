from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            if request.method in ['DELETE', 'POST']:
                return False
        return True


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user() == obj.owner:
            return True

