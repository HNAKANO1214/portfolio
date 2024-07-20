from django import forms

from myapp.models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
