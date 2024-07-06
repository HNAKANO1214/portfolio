import pytest
from django.core.management import call_command


@pytest.fixture(scope='session', autouse=True)
def load_seed_data(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        # シードデータをロードする
        print('Loading seed data...')
        call_command('loaddata', 'myapp/fixtures/seeders/work.json')
        print('Seed data loaded.')
