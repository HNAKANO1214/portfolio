from django import forms
from image_cropping import ImageCroppingMixin
from myapp.models import Profile


class ProfileForm(ImageCroppingMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
