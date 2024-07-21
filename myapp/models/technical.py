from django.db import models


class Technical(models.Model):
    """スキル"""
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100, default='', blank=True)
    percentage = models.IntegerField('パーセンテージ')
    order = models.IntegerField('表示順序', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'テクニカルスキル'
        verbose_name_plural = 'テクニカルスキル'
