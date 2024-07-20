import requests
import schedule
import time


def send_request():
    url = "https://portfolio-web-gjle.onrender.com/dummy_request/"
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 10分ごとに実行するようにスケジュール設定
schedule.every(10).minutes.do(send_request)

while True:
    schedule.run_pending()
    time.sleep(1)
