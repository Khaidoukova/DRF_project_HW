from rest_framework.permissions import  BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['view', 'update']:
            return True
        return request.user == view.get_object().owner