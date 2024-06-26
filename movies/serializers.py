from rest_framework import serializers
from .models import RatingChoices, Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_blank=True, default="")
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices,
        default=RatingChoices.G
    )
    synopsis = serializers.CharField(allow_blank=True, default="")

    added_by = serializers.SerializerMethodField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def get_added_by(self, movie: Movie):
        return movie.user.email