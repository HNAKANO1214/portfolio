import requests

from django.conf import settings


def dummy_request():
    # ダミーリクエストを送信
    url = f"{settings.SITE_BASE_URL}/dummy_request/"
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
