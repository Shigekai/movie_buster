from rest_framework import serializers
from .models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    title = serializers.SerializerMethodField()
    purchased_by = serializers.SerializerMethodField()
    purchased_at = serializers.DateTimeField(read_only=True)



    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
    
    def get_title(self, movie_order: MovieOrder):
        return movie_order.movie.title
    
    def get_purchased_by(self, movie_order: MovieOrder):
        return movie_order.user.email
    
