from django.db import models

from .worker import Worker


class Rating(models.Model):

    rating = models.FloatField("Rating")
    comment = models.CharField("Comment", max_length=500)

    worker_id = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="Worker"
    )

    def __str__(self):
        return f"{self.worker_id} - {self.rating}"
