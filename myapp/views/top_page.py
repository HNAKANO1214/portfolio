from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

from myapp.models import Profile, Work


class TopPageView(View):
    """トップページのビュー"""

    def get(self, request, *args, **kwargs):
        """get関数"""
        # クッキーの確認
        has_seen_animation = request.COOKIES.get('has_seen_animation')

        # プロフィールデータとワークデータの取得
        profile_data = Profile.get_query_all().order_by('-id').first()
        work_data = Work.get_query_all().order_by('-order', '-id')

        # テンプレートをレンダリング
        rendered_content = render(request, 'myapp/top_page.html', {
            'profile_data': profile_data,
            'work_data': work_data,
            'has_seen_animation': has_seen_animation,
        }).content
        response = HttpResponse(rendered_content)

        # クッキーにアニメーションフラグを設定
        if not has_seen_animation:
            response.set_cookie('has_seen_animation', 'true', max_age=3600)  # 1時間有効

        return response
