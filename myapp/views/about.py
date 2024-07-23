from django.views.decorators.cache import cache_page
from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator

from myapp.models import Profile, Experience, Education, Software, Technical


class AboutView(View):
    """プロフィールページのビュー"""

    @method_decorator(cache_page(60 * 15))
    def get(self, request, *args, **kwargs):
        """get関数"""
        profile_data = Profile.get_query_all().order_by('-id').first()
        experience_data = Experience.get_query_all().order_by('-order', '-id')
        education_data = Education.get_query_all().order_by('-order', '-id')
        software_data = Software.get_query_all().order_by('-order', '-id')
        technical_data = Technical.get_query_all().order_by('-order', '-id')
        return render(request, 'myapp/about.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data': education_data,
            'software_data': software_data,
            'technical_data': technical_data,
        })
