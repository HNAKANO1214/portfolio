from django.db import models
from django.utils.translation import get_language


class Education(models.Model):
    """学歴"""
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    period = models.CharField('期間', max_length=100)
    order = models.IntegerField('表示順序', default=0)
    language = models.CharField('言語', max_length=3, default='ja')

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = '学歴'
        verbose_name_plural = '学歴'

    @classmethod
    def get_query_all(cls):
        """カレント言語に基づく全データ取得"""
        return cls.objects.filter(language=get_language())
