from django.db import models

from .profession import Profession
from .user import User


class Worker(User):

    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)

    is_available = models.BooleanField("Availability")

    rating_number = models.IntegerField("Number of ratings", blank=True, null=True)

    rating = models.FloatField("Rating", blank=True, null=True) # TODO: Compute average

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"
