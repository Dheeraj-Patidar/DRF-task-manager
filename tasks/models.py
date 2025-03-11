from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


# Custom User Model
class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # points = models.PositiveIntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Update Task model
class Task(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("in-progress", "In Progress"),
        ("completed", "Completed"),
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        related_name="task",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
