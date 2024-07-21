# Generated by Django 4.2.9 on 2024-07-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_education_options_alter_experience_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='work',
            name='skill',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='スキル'),
        ),
    ]
