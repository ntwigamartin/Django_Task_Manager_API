from django.db import models

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
        max_length=3,
        choices=Priority.choices,
        default=Priority.LOW
    )
    status = models.CharField(
        max_length=4,
        choices=Status.choices,
        default=Status.CREATED
    )

    def __str__(self):
        return self.title
