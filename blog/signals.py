from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article


# Добавляем id в конец url, чтобы был всегда уникальный url
@receiver(post_save, sender=Article)
def added_id_in_url_field(sender, instance, created, **kwargs):
  if created:
    instance.url = '{0}-{1}'.format(instance.url, instance.id)
    instance.save()
    return

  last_element_url = instance.url.split('-')[-1]
  id = str(instance.id)
  if last_element_url != id:
    instance.url = '{0}-{1}'.format(instance.url, instance.id)
    instance.save()
