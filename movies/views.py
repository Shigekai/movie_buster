from rest_framework.views import Request, Response, status, APIView
from .models import Movie
from .serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import AllowEmployeeOrSafeMethod
from kenzie_buster.pagination import CustomPagination


class MovieView(APIView, CustomPagination):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowEmployeeOrSafeMethod,)


    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        paginated_movies = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(paginated_movies, many=True)


        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieIdView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (AllowEmployeeOrSafeMethod,)

    def get(self, request: Request, movie_id: int):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "Movie id is not valid"}, status.HTTP_400_BAD_REQUEST
                )
        
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)
    

    def delete(self, request: Request, movie_id: int):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"detail": "Movie id is not valid"}, status.HTTP_403_FORBIDDEN
                )
        
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
