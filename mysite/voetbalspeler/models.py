from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Voetbalspeler(models.Model):
    naamVoetballer = models.CharField('Naam van de voetballer', max_length=200)
    voetbalclub = models.CharField('Voetbalclub', max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title