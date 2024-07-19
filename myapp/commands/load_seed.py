
import os
import sys
import django
from django.core.management import call_command

sys.path.append(os.getcwd())
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'mysite.settings.local')
)
django.setup()

LOAD_SEED_DATA = [
    'myapp/fixtures/seeders/profile.json',
    'myapp/fixtures/seeders/work.json',
    'myapp/fixtures/seeders/education.json',
    'myapp/fixtures/seeders/experience.json',
    'myapp/fixtures/seeders/software.json',
    'myapp/fixtures/seeders/technical.json',
]


def load_seed_data():
    print('Loading seed data...')
    for seed_data in LOAD_SEED_DATA:
        print(f'Loading {seed_data}...')
        call_command('loaddata', seed_data)
        print(f'{seed_data} loaded.')
    print('Seed data loaded.')


if __name__ == '__main__':
    load_seed_data()
