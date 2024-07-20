from django.db import models


class Technical(models.Model):
    """スキル"""
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'スキル'
        verbose_name_plural = 'スキル'
