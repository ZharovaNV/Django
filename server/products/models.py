from django.db import models
from .utils import get_default_category

class Category(models.Model):
    sname = models.CharField(max_length=250)
    sdescription = models.TextField(null = True, blank = True)
    modified = models.DateTimeField (auto_now = True)
    created = models.DateTimeField(auto_now_add = True)


def __str__(self):
    return self.name

class Book(models.Model):
    sname = models.CharField(max_length=250)
    sauthor = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = get_default_category)
    image = models.ForeignKey('images.image',  on_delete = models.PROTECT, null = True, blank = True)
    nprice = models.DecimalField(max_digits=8, decimal_places=2)
    ncnt = models.DecimalField(max_digits=6, decimal_places=0)
    sshortdescr = models.TextField(null = True, blank = True)
    sfulldescr = models.TextField(null = True, blank = True)
    sagerestrict = models.CharField(max_length=3)
    sisbn =  models.CharField(max_length=30)
    npagecnt = models.DecimalField(max_digits=6, decimal_places=0)
    modified = models.DateTimeField (auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

@property
def is_modified (self):
    return self.is_modified != self.created

def __str__(self):
    return self.name