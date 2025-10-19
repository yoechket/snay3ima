from django.db import models


class Profession(models.Model):

    name = models.CharField("Profession name", max_length=20)
    description = models.TextField("Profession description", max_length=200)

    def __str__(self):
        return f"{self.name}"
