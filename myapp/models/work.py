from django.db import models


class Work(models.Model):
    """業務/作品"""
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to="images", verbose_name='イメージ画像')
    thumbnail = models.ImageField(
        upload_to="images", verbose_name='サムネイル', null='True', blank='True')
    skill = models.CharField('スキル', max_length=100, default='', blank=True)
    url = models.CharField('URL', max_length=100, null='True', blank='True')
    created = models.DateField('作成日')
    description = models.TextField('説明', default='', blank=True)
    order = models.IntegerField('表示順序', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '業務/作品'
        verbose_name_plural = '業務/作品'
