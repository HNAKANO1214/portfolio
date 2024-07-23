from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import get_language


class Profile(models.Model):
    '''プロフィール'''
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField(
        'サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField(
        'twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField(
        'linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField(
        'facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField(
        'instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')
    order = models.IntegerField('表示順序', default=0)
    language = models.CharField('言語', max_length=3, default='ja')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'プロフィール'
        verbose_name_plural = 'プロフィール'

    def delete(self, *args, **kwargs):
        if self.topimage:
            self.topimage.delete(save=False)
        if self.subimage:
            self.subimage.delete(save=False)
        super().delete(*args, **kwargs)

    @classmethod
    def get_query_all(cls):
        """カレント言語に基づく全データ取得"""
        return cls.objects.filter(language=get_language())


@receiver(post_save, sender=Profile)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_topimage = Profile.objects.get(pk=instance.pk).topimage
            old_subimage = Profile.objects.get(pk=instance.pk).subimage
        except Profile.DoesNotExist:
            return
        else:
            if old_topimage != instance.topimage:
                old_topimage.delete(save=False)
            if old_subimage != instance.subimage:
                old_subimage.delete(save=False)


@receiver(post_delete, sender=Profile)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.topimage:
        instance.topimage.delete(save=False)
    if instance.subimage:
        instance.subimage.delete(save=False)
