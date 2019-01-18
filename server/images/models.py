from django.db import models
from utility.models import DateTimeManager

class Image(DateTimeManager, models.Model):
    name = models.CharField(
        max_length=150
    )
    value = models.ImageField(
        upload_to='images'
    )

    @property
    def url(self):
        return self.value.url

    def __str__(self):
        return self.name