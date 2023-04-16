from django.utils import timezone
from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Portal(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)

    def launch(self):
        self.save()


class JobTitle(models.Model):
    title = models.CharField(max_length=250),
    last_updated = models.DateTimeField(default=timezone.now)
    portal = models.ForeignKey(Portal, on_delete=Portal)
