# ポートフォリオ

## 開発環境構築手順

1. **Dockerコンテナの起動します。**

    ```sh
    docker-compose up
2. **.envの配置**

    ```sh
    cp .env.local .env
3. **データベースのマイグレーションを実行します。**

    ```sh
    docker exec -it portfolio-web python manage.py migrate
4. **シードデータをロードします。**

    ※ 0からデータを作成する場合、この手順は不要です。

    ```sh
    docker exec -it portfolio-web python myapp/commands/load_seed.py
5. **スーパーユーザーを作成します。**

    ```sh
    docker exec -it portfolio-web python manage.py createsuperuser
## 自動テスト

```sh
docker exec -it portfolio-web pytest
