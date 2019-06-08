from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


# This are the breweries
class Brand(models.Model):
    date  = models.DateTimeField('Date of addition', default=timezone.now)
    name  = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

# This are the beers
class Item(models.Model):
    date  = models.DateTimeField('Date of addition', default=timezone.now)
    name  = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)

class Contest(models.Model):
    start_date = models.DateTimeField()
    end_date   = models.DateTimeField()
    name       = models.CharField(max_length=100)

class Role(models.Model):
    name  = models.CharField(max_length=100)
    level = models.IntegerField(default=5)

class ContestParticipant(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    user    = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role    = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    
class ContestItem(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    item    = models.ForeignKey(Item, on_delete=models.DO_NOTHING)

class ContestTable(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    name    = models.CharField(max_length=100)

class ContestTableItem(models.Model):
    table = models.ForeignKey(ContestTable, on_delete=models.DO_NOTHING)
    item  = models.ForeignKey(ContestItem, on_delete=models.DO_NOTHING)

