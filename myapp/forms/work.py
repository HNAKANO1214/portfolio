from django import forms

from myapp.models import Work


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
