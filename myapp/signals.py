from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.apps import apps
from django.db import models


def get_image_fields(instance):
    """Return all ImageField fields for a given instance."""
    return [field for field in instance._meta.get_fields() if isinstance(field, models.ImageField)]


@receiver(pre_save)
def delete_old_images(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    for field in get_image_fields(instance):
        old_file = getattr(old_instance, field.name)
        new_file = getattr(instance, field.name)
        if old_file and old_file != new_file:
            old_file.delete(save=False)


@receiver(post_delete)
def delete_images_on_delete(sender, instance, **kwargs):
    for field in get_image_fields(instance):
        image_file = getattr(instance, field.name)
        if image_file:
            image_file.delete(save=False)


def register_signals():
    for model in apps.get_models():
        if any(isinstance(field, models.ImageField) for field in model._meta.get_fields()):
            pre_save.connect(delete_old_images, sender=model)
            post_delete.connect(delete_images_on_delete, sender=model)


register_signals()
