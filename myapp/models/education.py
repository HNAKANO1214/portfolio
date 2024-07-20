from django.db import models


class Education(models.Model):
    """学歴"""
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = '学歴'
        verbose_name_plural = '学歴'
