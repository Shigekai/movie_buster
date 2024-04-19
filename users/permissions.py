from rest_framework.permissions import BasePermission
from rest_framework.views import Request, APIView
from .models import User

class AllowEmployeeOrOwner(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: User):
        return request.user.is_authenticated and \
               (request.user.is_employee or \
                request.user == obj)