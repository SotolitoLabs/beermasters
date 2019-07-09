from django.contrib import admin
from .models import  (Brand, Item, Contest, Role, ContestParticipant,
  ContestItem, ContestTable, ContestTableItem, Aroma, Apperance, Flavor, 
  Mouthfeel, DescriptorDefinition, ContestScoreSheet, 
  ContestScoreSheetDescriptor, ContestCategory, BJCPcategory, BJCPstyle)

# Register your models here.

admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(Contest)
admin.site.register(Role)
admin.site.register(Aroma)
admin.site.register(Apperance)
admin.site.register(Flavor)
admin.site.register(Mouthfeel)
admin.site.register(DescriptorDefinition)
admin.site.register(ContestScoreSheet)
admin.site.register(ContestScoreSheetDescriptor)
admin.site.register(ContestParticipant)
admin.site.register(ContestItem)
admin.site.register(ContestTable)
admin.site.register(ContestTableItem)
admin.site.register(ContestCategory)
admin.site.register(BJCPcategory)
admin.site.register(BJCPstyle)
