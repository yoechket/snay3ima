from django.contrib import admin

from .models.city import City
from .models.intervention import Intervention
from .models.profession import Profession
from .models.rating import Rating
from .models.task_rating import TaskRating
from .models.task import Task
from .models.user import User
from .models.worker import Worker


admin.site.register(City)


admin.site.register(Intervention)


admin.site.register(Profession)


admin.site.register(Rating)


admin.site.register(TaskRating)


admin.site.register(Task)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "last_name",
        "first_name",
        "email",
        "birthday",
        "phoneNumber",
        "city_id"
    )


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "last_name",
        "first_name",
        "email",
        "birthday",
        "phoneNumber",
        "city_id",
        "profession_id",
        "is_available",
        "rating_number",
        "rating"
    )
