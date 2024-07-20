from django import forms

from myapp.models import Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
