from rest_framework import serializers

from snay3i.models.worker import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profession_id']
