from django.urls import path, include

from rest_framework.routers import DefaultRouter

from snay3i.views.city import CityViewSet
from snay3i.views.intervention import InterventionViewSet
from snay3i.views.profession import ProfessionViewSet
from snay3i.views.rating import RatingViewSet
from snay3i.views.task_rating import TaskRatingViewSet
from snay3i.views.task import TaskViewSet
from snay3i.views.user import UserViewSet
from snay3i.views.worker import WorkerViewSet


router = DefaultRouter()
router.register(r'cities', CityViewSet, basename='city')
router.register(r'interventions', InterventionViewSet, basename='intervention')
router.register(r'professions', ProfessionViewSet, basename='profession')
router.register(r'ratings', RatingViewSet, basename='rating')
router.register(r'task-ratings', TaskRatingViewSet, basename='task-rating')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')
router.register(r'workers', WorkerViewSet, basename='worker')

# API endpoints
urlpatterns = [
    path('', include(router.urls))
]
