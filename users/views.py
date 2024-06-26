from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import get_object_or_404
from .permissions import AllowEmployeeOrOwner
from users.serializers import UserSerializer
from .models import User

class UserView(APIView):

    def post(self, request:Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    
class UserIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowEmployeeOrOwner]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User.objects.all(), pk=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User.objects.all(), pk=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)






