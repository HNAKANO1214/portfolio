from django.http import JsonResponse
from django.views import View


class DummyRequestView(View):
    """ダミーリクエストビュー

        Renderの無料版は15分リクエストがないとスリープするため、
        ダミーリクエストを受信するAPIを作成
        空のJSONレスポンスを返却する
    """

    def get(self, request, *args, **kwargs):
        """get関数"""
        # JSONレスポンスを返却
        return JsonResponse({})
