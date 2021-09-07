from rest_framework import permissions as pm


class IsOwnerOrAdmin(pm.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True

        return bool(
            request.user
            and (request.user.is_admin
                 or request.user.is_staff))


class IsAuthenticated(pm.BasePermission):

    def has_permission(self, request, view):
        if all((view.kwargs.get('username') == 'me',
                request.user.is_authenticated)):
            return True

        return bool(
            request.user and request.user.is_authenticated
            and (request.user.is_admin or request.user.is_staff))
