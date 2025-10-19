from django.db import models

from .task import Task
from .user import User
from .worker import Worker

STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]


class Intervention(models.Model):

    worker_id = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='worker_interventions'
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_interventions')

    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

    location = models.CharField("Intervention location", max_length=100)

    status = models.CharField(
        "Intervention status",
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    start_datetime = models.DateTimeField("Intervention datetime")
    rating = models.IntegerField("Intervention rating", default=0)
    comment = models.CharField("Intervention comment", max_length=500)

# TODO: turn all following methods into API CALLS from front

    def create(self, **kwargs):
        self.status = 'pending'
        self.worker_id = kwargs.get('worker_id')
        self.user_id = kwargs.get('user_id')
        self.save()

    def approve(self):
        if self.status != 'pending':
            raise ValueError("Intervention cannot be approved unless it's pending.")
        self.status = 'approved'
        self.save()

    def reject(self):
        if self.status != 'pending':
            raise ValueError("Intervention cannot be rejected unless it's pending.")
        self.status = 'rejected'
        self.save()

    def start(self):
        if self.status != 'approved':
            raise ValueError("Intervention cannot be started unless it's in approved status.")
        self.status = 'in_progress'
        self.save()

    def complete(self):
        if self.status != 'in_progress':
            raise ValueError("Intervention cannot be completed unless it's in progress.")
        self.status = 'completed'
        if self.rating <= 0:
            raise ValueError("Intervention cannot be completed without a valid rating.")
        self.save()

    def cancel(self):
        if self.status == 'completed':
            raise ValueError("Intervention cannot be cancelled after completion.")
        self.status = 'cancelled'
        self.save()
