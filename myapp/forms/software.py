from django import forms

from myapp.models import Software


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
