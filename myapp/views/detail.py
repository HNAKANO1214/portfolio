from django.views.generic import View
from django.shortcuts import render

from myapp.models import Work


class DetailView(View):
    """業務/作品詳細ページのビュー"""

    def get(self, request, *args, **kwargs):
        """get関数

        Args:
            request (HttpRequest): リクエスト
            *args: 任意の引数
            **kwargs:
                pk: 取得データのID(必須)
                任意の引数
        """
        work_data = Work.objects.get(id=self.kwargs['pk'])
        return render(request, 'myapp/detail.html', {
            'work_data': work_data
        })
