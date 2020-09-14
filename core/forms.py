from django import forms
from core.models import StartUpInternships

class StartUpInternshipModelForm(forms.ModelForm):
    class Meta:
        model = StartUpInternships
        fields = '__all__'