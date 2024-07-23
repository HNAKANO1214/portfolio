from django.db import models
from django.utils.translation import get_language


class Technical(models.Model):
    """スキル"""
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100, default='', blank=True)
    percentage = models.IntegerField('パーセンテージ')
    order = models.IntegerField('表示順序', default=0)
    language = models.CharField('言語', max_length=3, default='ja')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'テクニカルスキル'
        verbose_name_plural = 'テクニカルスキル'

    @classmethod
    def get_query_all(cls):
        """カレント言語に基づく全データ取得"""
        return cls.objects.filter(language=get_language())
