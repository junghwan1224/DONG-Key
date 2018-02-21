from django.db import models
from django.dispatch import receiver
from django.conf import settings
from finance.models import Accounting
from django.core.signals import request_finished


class Club(models.Model):
    name = models.CharField(
            max_length=50,
            verbose_name='club name',
        )
    image = models.ImageField(
            upload_to='club/%Y/%m/%d/',
            blank=True,
            null=True,
        )
    description = models.TextField(
            verbose_name='club description',
            blank=True,
            null=True,
        )

    def __str__(self):
        return self.name


@receiver(models.signals.post_save, sender=Club)
def create_accounting(sender, instance, **kwargs):
    if not hasattr(instance, 'accounting'):
        Accounting.objects.create(club=instance)


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


class ApplyList(models.Model):
    club = models.ForeignKey(
            Club,
            on_delete=models.CASCADE,
        )
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )

    def __str__(self):
        return '{0} : {1}'.format(self.club, self.user)


class ClubRule(models.Model):
    main_theme = models.CharField(
            max_length=30,
            verbose_name='main theme',
        )
    sub_theme = models.CharField(
            max_length=30,
            verbose_name='sub theme',
            blank=True,
            null=True,
        )
    rule = models.TextField(verbose_name='rule')
    club = models.ForeignKey(
            Club,
            on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.main_theme
