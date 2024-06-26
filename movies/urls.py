from django.urls import path
from .views import MovieView, MovieIdView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/",MovieIdView.as_view())
]
