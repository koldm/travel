from django.db import models
from geo.models import Region, City
from users.models import User
from attraction.models import Attraction

class ExcursionMeetingPoint(models.Model):
  text = models.TextField('Описание места встречи', blank=True)
  # тут гео точки
  
  class Meta:
    verbose_name = 'Место встречи'
    verbose_name_plural = 'Места встречи'

  def __str__(self):
    return self.text


class ExcursionCategory(models.Model):
  name = models.CharField('Название', max_length=255)
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=True)
  
  class Meta:
    verbose_name = 'Категория экскурсии'
    verbose_name_plural = 'Категории экскурсий'
  
  def __str__(self):
    return self.name


class ExcursionType(models.Model):
  name = models.CharField('Название', max_length=255)
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=True)
  
  class Meta:
    verbose_name = 'Тип экскурсии'
    verbose_name_plural = 'Типы экскурсий'
  
  def __str__(self):
    return self.name


class ExcursionMovement(models.Model):
  name = models.CharField('Название', max_length=255)
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=True)
  
  class Meta:
    verbose_name = 'Способ передвижения'
    verbose_name_plural = 'Способы передвижения'
  
  def __str__(self):
    return self.name


class Excursion(models.Model):
  PRICE_TYPE_CHOICES = [
    ('PE', 'С человека'), # person
    ('TO', 'За экскурсию'), # tour
  ]
  name = models.CharField('Название экскурсии', max_length=255)
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=False)
  region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Область/край')
  city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город')
  title = models.CharField('SEO - Title', max_length=255, blank=True)
  description = models.CharField('SEO - Description', max_length=255, blank=True)
  keywords = models.CharField('SEO - Keywords', max_length=255, blank=True)
  preview_text = models.TextField('Превью описание', blank=True)
  detail_text = models.TextField('Описание экскурсии', blank=True)
  author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Автор')
  meeting_point = models.ForeignKey(ExcursionMeetingPoint, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Место встречи')
  price = models.PositiveIntegerField('Цена', blank=True, null=True)
  price_type = models.CharField('Тип цены', max_length=2, choices=PRICE_TYPE_CHOICES, blank=True)
  categories = models.ManyToManyField(ExcursionCategory, verbose_name='Категории')
  type = models.ForeignKey(ExcursionType, on_delete=models.SET_NULL, blank=True, null=True)
  movement = models.ForeignKey(ExcursionMovement, on_delete=models.SET_NULL, blank=True, null=True)
  children = models.BooleanField('Можно с детьми', default=True)
  max_piople_group = models.PositiveSmallIntegerField('Кол-во людей в группе', blank=True, null=True)
  include = models.JSONField('Что включено', blank=True, null=True)
  not_include = models.JSONField('Что не включено', blank=True, null=True)
  duration_time = models.PositiveIntegerField('Длительность, в минутах', blank=True, null=True)
  #photos
  average_rating = models.FloatField('Средний рейтинг', blank=True, null=True)
  attractions = models.ManyToManyField(Attraction, blank=True, verbose_name='Достопримечательности')
  
  class Meta:
    verbose_name = 'Экскурсия'
    verbose_name_plural = 'Экскурсии'
  
  def __str__(self):
    return self.name


class ExcursionReview(models.Model):
  STATUS_CHOICES = [
    ('RE', 'Удален'),
    ('MO', 'Модерация'),
    ('PU', 'Опубликован'),
  ]
  review = models.TextField('Отзыв')
  rating = models.PositiveSmallIntegerField('Рейтинг от 1 до 5')
  author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Автор отзыва')
  date_created = models.DateField('Дата отзыва', auto_now_add=True)
  status = models.CharField('Статус отзыва', max_length=2, choices=STATUS_CHOICES)
  # photos
  excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name='Экскурсия')
  
  class Meta:
    verbose_name = 'Отзыв'
    verbose_name_plural = 'Отзывы'
  
  def __str__(self):
    return self.review


class ExcursionFaq(models.Model):
  question = models.TextField('Вопрос')
  author_question = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
  answer = models.TextField('Ответ')
  excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, verbose_name='Вопрос/Ответ')
  
  class Meta:
    verbose_name = 'Вопрос/Ответ'
    verbose_name_plural = 'Вопросы/Ответы'
  
  def __str__(self):
    return self.question
