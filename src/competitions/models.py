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

# This is the categories catalog
class BJCPcategory(models.Model):
    date     = models.DateTimeField('Date of addition', default=timezone.now)
    name     = models.TextField()
    def __str__(self):
        return self.name


# This is the styles catalog.
class BJCPstyle(models.Model):
    date     = models.DateTimeField('Date of addition', default=timezone.now)
    name     = models.TextField()
    category = models.ForeignKey(BJCPcategory, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

# This are the beers
class Item(models.Model):
    date  = models.DateTimeField('Date of addition', default=timezone.now)
    name  = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    style = models.ForeignKey(BJCPstyle, on_delete=models.DO_NOTHING)
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

# In order to avoid confusing app Users versus django auth Users, we'll refer to
# the first ones as EndUsers, here we'll define the model
class EndUser(models.Model):
    user   = models.ForeignKey(User, unique=True, on_delete=models.DO_NOTHING)
    bjcp_id = models.CharField(max_length=15, blank=True, default='')
    elegibleforjudge = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


# To avoid complexity on the database consider this sensorial attributes
# as objects, the rarely change so they can be table fields
# instead of creating an attribute table and more complex relations

class Aroma(models.Model):
    score         = models.IntegerField()
    malt          = models.IntegerField()
    hop           = models.IntegerField()
    fermentation  = models.IntegerField()
    other         = models.TextField()
    comment       = models.TextField()

class Apperance(models.Model):
    score     = models.IntegerField()
    color     = models.IntegerField()
    transp    = models.IntegerField()
    other     = models.TextField()
    comment   = models.TextField()

class Flavor(models.Model):
    score        = models.IntegerField()
    malt         = models.IntegerField()
    hop          = models.IntegerField()
    bitterness   = models.IntegerField()
    fermentation = models.IntegerField()
    balance      = models.IntegerField()
    final        = models.IntegerField()
    other        = models.TextField()
    comment      = models.TextField()

class Mouthfeel(models.Model):
    score       = models.IntegerField()
    body        = models.IntegerField()
    carbonation = models.IntegerField()
    warmth      = models.IntegerField()
    creaminess  = models.IntegerField()
    astringency = models.IntegerField()
    other       = models.TextField()
    comment     = models.TextField()


class DescriptorDefinition(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
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

class ContestCategory(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    name    = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ContestTable(models.Model):
    contest  = models.ForeignKey(Contest, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(ContestCategory, blank=True, null=True, on_delete=models.DO_NOTHING)
    name     = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ContestTableItem(models.Model):
    table = models.ForeignKey(ContestTable, on_delete=models.DO_NOTHING)
    item  = models.ForeignKey(ContestItem, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.item.item.name

class ContestScoreSheet(models.Model):
    table_item          = models.ForeignKey(ContestTableItem, on_delete=models.DO_NOTHING)
    aroma               = models.ForeignKey(Aroma, on_delete=models.DO_NOTHING)
    apperance           = models.ForeignKey(Apperance, on_delete=models.DO_NOTHING)
    flavor              = models.ForeignKey(Flavor, on_delete=models.DO_NOTHING)
    mouthfeel           = models.ForeignKey(Mouthfeel, on_delete=models.DO_NOTHING)
    special_ingredients = models.CharField(max_length=200)
    bottle_insp         = models.NullBooleanField()
    bottle_insp_comment = models.TextField()
    overall_score       = models.IntegerField()
    overall_comment     = models.TextField()
    style               = models.IntegerField()
    technical           = models.IntegerField()
    intangible          = models.IntegerField()
    total_score         = models.IntegerField()
    def __str__(self):
        return "%s on %s" % (self.table_item.item.item.name, self.table_item.table.name)


class ContestScoreSheetDescriptor(models.Model):
    score_sheet = models.ForeignKey(ContestScoreSheet, on_delete=models.DO_NOTHING)
    descriptor  =  models.ForeignKey(DescriptorDefinition, on_delete=models.DO_NOTHING)

#class BjcpRank(models.Model):
#    name = models.CharField(max_length=100)
#    def __str__(self):
#        return self.name

#class UserBjcpInfo(models.Model):
#    bjcp_id = models.IntegerField(default=0)
#    bjcp_rank  = models.ForeignKey(BjcpRank, on_delete=models.DO_NOTHING)




#TODO check subcategories
#NAME = subcategory" type="text
#NAME = entry" type="text" value="{{ table_item.id }}" placeholder="Entry
#NAME = subcategory" type="text




