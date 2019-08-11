from django import forms
from competitions.models import EndUser

class BrewerapplyForm(forms.ModelForm):
    bjcp_id = forms.CharField(max_length=20)

    class Meta:
        model = EndUser
        fields = ('bjcp_id',)
