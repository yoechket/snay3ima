from django.db import models

from .task import Task
from .user import User


class TaskRating(models.Model):

    rating = models.FloatField("Task rating")
    comment = models.CharField("Comment", max_length=500)

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="User"
    )

    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="Task")

    def __str__(self):
        return f"{self.task_id} - {self.rating}"
