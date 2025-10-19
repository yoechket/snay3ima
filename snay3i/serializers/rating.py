from rest_framework import serializers

from snay3i.models.rating import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating', 'comment', 'worker_id']
