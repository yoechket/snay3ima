from rest_framework import serializers

from snay3i.models.city import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']
