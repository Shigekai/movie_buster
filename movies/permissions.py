from rest_framework.permissions import BasePermission, SAFE_METHODS

class AllowEmployeeOrSafeMethod(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS\
                or \
                (request.user.is_authenticated and request.user.is_employee) 