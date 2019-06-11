from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


# This are the breweries
class Brand(models.Model):
    date  = models.DateTimeField('Date of addition', default=timezone.now)
    name  = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

# This are the beers
class Item(models.Model):
    date  = models.DateTimeField('Date of addition', default=timezone.now)
    name  = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Contest(models.Model):
    start_date = models.DateTimeField()
    end_date   = models.DateTimeField()
    name       = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Role(models.Model):
    name  = models.CharField(max_length=100)
    level = models.IntegerField(default=5)
    def __str__(self):
        return self.name

class ContestParticipant(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    user    = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role    = models.ForeignKey(Role, on_delete=models.DO_NOTHING)
    def __str__(self):
        return "%s at %s (%s)" % (self.user, self.contest, self.role)
    
class ContestItem(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    item    = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.item.name

class ContestTable(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    name    = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ContestTableItem(models.Model):
    table = models.ForeignKey(ContestTable, on_delete=models.DO_NOTHING)
    item  = models.ForeignKey(ContestItem, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.item.item.name

