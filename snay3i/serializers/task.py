from rest_framework import serializers

from snay3i.models.task import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'price', 'rating_number', 'profession_id', 'worker_id']
