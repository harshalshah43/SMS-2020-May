from .models import Answer

from django import forms

class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['title','course','subject','content','pdf']