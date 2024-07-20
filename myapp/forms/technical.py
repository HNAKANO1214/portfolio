from django import forms

from myapp.models import Technical


class TechnicalForm(forms.ModelForm):
    class Meta:
        model = Technical
        fields = '__all__'
