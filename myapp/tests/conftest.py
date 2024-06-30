import pytest
from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup():
    pass


@pytest.fixture(scope='function')
def load_seed_data(db):
    # シードデータをロードする
    # TODO: 調整必要
    # call_command('loaddata', 'myapp/fixtures/seeders/work.json')
    pass
