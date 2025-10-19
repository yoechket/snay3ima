from django.db import models


class City(models.Model):

    name = models.CharField(verbose_name="City name", max_length=20)

    class Meta:
        verbose_name = "City"
        ordering = ['name']
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name}"
