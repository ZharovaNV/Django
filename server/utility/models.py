from django.db import models

class DateTimeManager(models.Model):
    modified = models.DateTimeField(
        auto_now=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    
    class Meta:
        abstract=True

