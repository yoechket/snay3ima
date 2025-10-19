from django.db import models
from django.utils import timezone

from datetime import date

from dateutil.relativedelta import relativedelta

from .city import City


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import date
from dateutil.relativedelta import relativedelta
from .city import City


class User(AbstractUser):

    birthday = models.DateField("Birthday", blank=True, null=True)
    phoneNumber = models.CharField("Phone Number", max_length=20, blank=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=False)
    creationDate = models.DateField("Account creation date", default=timezone.now)

    @property
    def get_age(self):
        if self.birthday:
            return relativedelta(date.today(), self.birthday).years
        return 0

    def save(self, *args, **kwargs):
        self.age = self.get_age
        super(User, self).save(*args, **kwargs)
