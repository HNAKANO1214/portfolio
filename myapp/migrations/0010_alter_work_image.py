# Generated by Django 4.2.9 on 2024-07-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_education_language_experience_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank='True', null='True', upload_to='images', verbose_name='イメージ画像'),
        ),
    ]
