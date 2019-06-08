from django.contrib import admin
from .models import  (Brand, Item, Contest, Role, ContestParticipant,
  ContestItem, ContestTable, ContestTableItem)

# Register your models here.

admin.site.register(Brand)
admin.site.register(Item)
admin.site.register(Contest)
admin.site.register(Role)
admin.site.register(ContestParticipant)
admin.site.register(ContestItem)
admin.site.register(ContestTable)
admin.site.register(ContestTableItem)
