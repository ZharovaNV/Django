from django.db import models

class Book(models.Model):
    sname = models.CharField(max_length=250)
    sauthor = models.CharField(max_length=250)
    nprice = models.DecimalField(max_digits=8, decimal_places=2)
    ncnt = models.DecimalField(max_digits=6, decimal_places=0)
    sshortdescr = models.TextField()
    sfulldescr = models.TextField()
    sagerestrict = models.CharField(max_length=3)
    sisbn =  models.CharField(max_length=30)
    npagecnt = models.DecimalField(max_digits=6, decimal_places=0)
