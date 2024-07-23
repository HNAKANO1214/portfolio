from django.views.generic import View
from django.shortcuts import render

from myapp.models import Profile, Work


class TopPageView(View):
    """トップページのビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        profile_data = Profile.get_query_all().order_by('-id').first()
        work_data = Work.get_query_all().order_by('-order', '-id')
        return render(request, 'myapp/top_page.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })
