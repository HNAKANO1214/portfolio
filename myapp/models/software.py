from django.db import models


class Software(models.Model):
    """ソフトウェア"""
    name = models.CharField('ソフトウェア', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ソフトウェア'
        verbose_name_plural = 'ソフトウェア'
