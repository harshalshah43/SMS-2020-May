from django import forms 
from .models import Activity

class ActivityCreateForm(forms.ModelForm):
    class Meta:
        model =Activity
        fields=['title','content','date_posted','expires_on','pdf']