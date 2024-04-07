from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone
    
class User(AbstractUser):
    referral_code = models.CharField(max_length=20, blank=True, null=True)
    timestamp_of_registration = models.DateTimeField(default=timezone.now)