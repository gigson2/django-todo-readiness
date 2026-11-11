from django.db import models
from django.utils import timezone


class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ("due_date", "id")

    def __str__(self):
        return f"{self.text}: due {self.due_date}"
