from builtins import dict
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


import uuid


class Job(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gamma = models.DecimalField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1),
        ],
        decimal_places=4,
        max_digits=5,
        blank=False,
        null=False,
    )
    qpu = models.BooleanField(default=False)
    theta = models.DecimalField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1),
        ],
        decimal_places=4,
        max_digits=5,
        blank=False,
        null=False,
    )
    phi = models.DecimalField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1),
        ],
        decimal_places=4,
        max_digits=5,
        blank=False,
        null=False,
    )
