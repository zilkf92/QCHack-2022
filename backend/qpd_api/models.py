from builtins import dict
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


import uuid


class Strategy(models.Model):

    theta = models.DecimalField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1),
        ],
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True,
    )

    phi = models.DecimalField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1),
        ],
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True,
    )


class Settings(models.Model):

    gamma = models.DecimalField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1),
        ],
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True,
    )

    qpu = models.BooleanField(default=False)


class Job(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    settings = models.ForeignKey(
        "Settings", on_delete=models.CASCADE, blank=True, null=True
    )
    strategy = models.ForeignKey(
        "Strategy", on_delete=models.CASCADE, blank=True, null=True
    )
