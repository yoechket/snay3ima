from rest_framework import serializers

from snay3i.models.task_rating import TaskRating


class TaskRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRating
        fields = ['rating', 'comment', 'user_id', 'task_id']
