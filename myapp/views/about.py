from django.views.generic import View
from django.shortcuts import render

from myapp.models import Profile, Experience, Education, Software, Technical


class AboutView(View):
    """プロフィールページのビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        experience_data = Experience.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        return render(request, 'myapp/about.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data': education_data,
            'software_data': software_data,
            'technical_data': technical_data,
        })
