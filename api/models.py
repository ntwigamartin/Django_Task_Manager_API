from django.db import models
from django.utils import timezone

class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'Low'
        MEDIUM = 'Medium'
        HIGH = 'High'

    class Status(models.TextChoices):
        CREATED = 'Created'
        STARTED = 'Started'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'

    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(
        max_length=6,
        choices=Priority.choices,
        default=Priority.LOW
    )
    status = models.CharField(
        max_length=9,
        choices=Status.choices,
        default=Status.CREATED
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
