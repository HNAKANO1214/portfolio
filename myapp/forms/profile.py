from django import forms

from myapp.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        models = Profile
        fields = '__all__'
