from django.db import models
from django.utils.translation import get_language


class Experience(models.Model):
    """職歴"""
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    period = models.CharField('期間', max_length=100)
    order = models.IntegerField('表示順序', default=0)
    language = models.CharField('言語', max_length=3, default='ja')

    def __str__(self):
        return self.occupation

    class Meta:
        verbose_name = '職歴'
        verbose_name_plural = '職歴'

    @classmethod
    def get_query_all(cls):
        """カレント言語に基づく全データ取得"""
        return cls.objects.filter(language=get_language())
