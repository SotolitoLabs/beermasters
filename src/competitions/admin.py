from django.contrib import admin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.translation import ugettext_lazy as _



from .models import  (Brand, Item, Contest, Role, ContestParticipant,
  ContestItem, ContestTable, ContestTableItem, Aroma, Apperance, Flavor, 
  Mouthfeel, DescriptorDefinition, ContestScoreSheet, 
  ContestScoreSheetDescriptor, ContestCategory, BJCPcategory, BJCPstyle, EndUser,
  ContestCategoryStyle)

# add extra fields to the Django Admin Add User form using UserCreationForm
# ref:  https://gist.github.com/riklomas/511440

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75)

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'username', 'first_name', 'last_name', 'is_active', 'password1', 'password2',)
    }),
)

class ContestCategoryStyleInline(admin.TabularInline):
    model = ContestCategoryStyle
    extra = 1

class ContestCategoryAdmin(admin.ModelAdmin):
    inlines = (ContestCategoryStyleInline,)

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
admin.site.register(BJCPcategory)
admin.site.register(BJCPstyle)
admin.site.register(EndUser)
admin.site.register(ContestCategoryStyle)
admin.site.register(ContestCategory, ContestCategoryAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
