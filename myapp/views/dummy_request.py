from django.http import JsonResponse
from django.views import View


class DummyRequestView(View):
    """ダミーリクエストビュー

        空のレスポンスを返却
        renderの休眠対策として定期的にリクエストを送信する仕組みを採用しているが、
        可能な限り通信量を減らすためのAPIとして利用する
    """

    def get(self, request, *args, **kwargs):
        """get関数"""
        # JSONレスポンスを返却
        return JsonResponse({})
