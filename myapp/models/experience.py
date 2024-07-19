from django.db import models


class Experience(models.Model):
    """職歴"""
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation
