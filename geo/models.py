from django.db import models


class Region(models.Model):
  name = models.CharField('Название области', max_length=255, unique=True)
  name_pr = models.CharField('Название области в предложном падеже', max_length=255, blank=True)
  is_active = models.BooleanField('Активность', default=True)
  url = models.SlugField('URL', max_length=255, unique=True, db_index=True)
  # photo
  
  class Meta:
    ordering = ['name']
    verbose_name = 'Область/край'
    verbose_name_plural = 'Области/края'
  
  def __str__(self):
    return self.name


class City(models.Model):
  name = models.CharField('Название города', max_length=255, unique=True)
  name_pr = models.CharField('Название города в предложном падеже', max_length=255, blank=True)
  is_active = models.BooleanField('Активность', default=True)
  url = models.SlugField('URL', max_length=255, unique=True, db_index=True)
  region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Область/край', blank=True, null=True)
  
  class Meta:
    ordering = ['name']
    verbose_name = 'Город'
    verbose_name_plural = 'Города'
  
  def __str__(self):
    return self.name
