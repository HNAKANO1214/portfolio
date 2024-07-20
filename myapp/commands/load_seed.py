
import django
import os
import shutil
import sys

from dotenv import load_dotenv

from django.core.management import call_command

sys.path.append(os.getcwd())
load_dotenv()
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'config.settings.local')
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


def load_images():
    print('Loading images...')
    # media/images/ が存在しない場合は作成
    if not os.path.exists('media/images'):
        os.makedirs('media/images')
    for image in os.listdir('myapp/fixtures/seeders/images'):
        print(f'Loading {image}...')
        # 同じファイル名がある場合はスキップ
        if os.path.exists(f'media/images/{image}'):
            print(f'{image} already exists. Skipped.')
            continue
        shutil.copyfile(f'myapp/fixtures/seeders/images/{image}', f'media/images/{image}')
        print(f'{image} loaded.')
    print('Images loaded.')


if __name__ == '__main__':
    load_seed_data()
    load_images()
