from django.db import models
from django.contrib.auth.models import AbstracUser

# Create your models here.

class User(AbstracUser):
    """Extiende el Usuario de django"""
