from django.views.generic import View
from django.shortcuts import render

from myapp.models import Profile, Work


class TopPageView(View):
    """トップページのビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        profile_data = Profile.objects.all()
        if profile_data.exists():
            # idを降順に並べ替え、最新のプロフィールデータを取得
            profile_data = profile_data.order_by('-id')[0]
        # orderを昇順、IDを昇順に並べ替え、最新の業務/作品データを取得
        work_data = Work.objects.order_by('-order', '-id')
        return render(request, 'myapp/top_page.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })
