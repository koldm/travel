from django.db import models


class SeoTemplate(models.Model):
  title = models.CharField('Title', max_length=255)
  description = models.CharField('Description', max_length=255)
  keywords = models.CharField('Keywords', max_length=255)
  type = models.CharField('Тип, берем из get=types', max_length=255, unique=True)
  og = models.JSONField('Open Graph разметка', blank=True)
  helper = models.TextField('Описание шаблона для админа')
  
  class Meta:
    verbose_name = 'SEO шаблон'
    verbose_name_plural = 'SEO шаблоны'
    
  def __str__(self):
    return self.helper


class Seo(models.Model):
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=True)
  title = models.CharField('Title', max_length=255)
  description = models.CharField('Description', max_length=255)
  keywords = models.CharField('Keywords', max_length=255, blank=True)
  og = models.JSONField('Open Graph разметка', blank=True)
  
  class Meta:
    verbose_name = 'SEO'
    verbose_name_plural = 'SEO'
  
  def __str__(self):
    return self.url



    