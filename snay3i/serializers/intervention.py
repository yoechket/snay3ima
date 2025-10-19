from rest_framework import serializers

from snay3i.models.intervention import Intervention


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = [
            'worker_id',
            'user_id',
            'task_id',
            'location',
            'status',
            'start_datetime',
            'rating',
            'comment'
        ]
