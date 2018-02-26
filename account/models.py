from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )
    school = models.CharField(
            max_length=20,
            verbose_name='member school',
        )
    phone_number = models.CharField(
            max_length=20,
            verbose_name='phone number',
        )
