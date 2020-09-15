from django import forms
from core.models import StartUpInternships

class StartUpInternshipModelForm(forms.ModelForm):
    class Meta:
        model = StartUpInternships
        fields = '__all__'
        widgets = {
            'last_date_to_apply': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
        }