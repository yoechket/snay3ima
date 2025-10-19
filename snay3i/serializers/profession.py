from rest_framework import serializers

from snay3i.models.profession import Profession


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = [
            'name',
            'description'
        ]
