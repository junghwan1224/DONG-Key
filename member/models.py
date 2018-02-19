from django.db import models
# from django.contrib.auth.models import User
from club.models import Club
from django.conf import settings
# Create your models here.


class Member(models.Model):
    club = models.ForeignKey(
            Club,
            on_delete=models.CASCADE,
        )
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )
    is_admin = models.BooleanField(
            default=False,
        )
    # positon False=member, True=admin
