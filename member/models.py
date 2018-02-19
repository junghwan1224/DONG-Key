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


class Attendance(models.Model):
    member = models.ForeignKey(
            Member,
            on_delete=models.CASCADE,
        )
    attendance_check = models.BooleanField(
            default=False,
        )
    attendance_date = models.DateTimeField(
            auto_now_add=True,
            verbose_name='attendance date',
        )


class Absence(models.Model):
    attendance = models.OneToOneField(
            Attendance,
            on_delete=models.CASCADE,
        )
    minus = models.IntegerField(
            default=0,
        )
    minus_reason = models.CharField(
            max_length=100,
            verbose_name='minus reason',
        )
