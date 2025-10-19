from django.db import models

from .profession import Profession
from .worker import Worker


class Task(models.Model):

    name = models.CharField("Task name", max_length=20)
    description = models.TextField("Task description", max_length=200)
    price = models.FloatField("Task price", max_length=20)

    rating_number = models.IntegerField("Number of ratings", default=0)

    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
