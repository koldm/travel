from django.db import models
from geo.models import Region, City
from users.models import User


class AttractionType(models.Model):
  name = models.CharField('Название', max_length=255, unique=True)
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=True)
  
  class Meta:
    verbose_name = 'Тип достопримечательности'
    verbose_name_plural = 'Типы достопримечательностей'
  
  def __str__(self):
    return self.name


class Attraction(models.Model):
  name = models.CharField('Название достопримечательности', max_length=255)
  url = models.CharField('URL', max_length=255)
  is_active = models.BooleanField('Активность', default=False)
  region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Область/край')
  city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Город')
  title = models.CharField('SEO - Title', max_length=255, blank=True)
  description = models.CharField('SEO - Description', max_length=255, blank=True)
  keywords = models.CharField('SEO - Keywords', max_length=255, blank=True)
  preview_text = models.TextField('Превью описание', blank=True)
  detail_text = models.TextField('Описание достопримечательности', blank=True)
  # координаты
  # photos
  types = models.ManyToManyField(AttractionType, blank=True, verbose_name='Тип достопримечательности')
  average_rating = models.FloatField('Средний рейтинг', blank=True, null=True)
  count_reviews = models.PositiveIntegerField('Кол-во отзывов', blank=True, null=True)
  
  class Meta:
    verbose_name = 'Достопримечательность'
    verbose_name_plural = 'Достопримечательности'
  
  def __str__(self):
    return self.name


class AttractionReview(models.Model):
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
  attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, verbose_name='Достопримечательность')
  
  class Meta:
    verbose_name = 'Отзыв'
    verbose_name_plural = 'Отзывы'
  
  def __str__(self):
    return self.review


class AttractionFaq(models.Model):
  STATUS_CHOICES = [
    ('RE', 'Удален'),
    ('MO', 'Модерация'),
    ('PU', 'Опубликован'),
  ]
  status = models.CharField('Статус вопроса', max_length=2, choices=STATUS_CHOICES)
  date_created = models.DateField('Дата отзыва', auto_now_add=True)
  question = models.TextField('Вопрос')
  author_question = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
    related_name='author_question',
    verbose_name='Автор вопроса'
  )
  answer = models.TextField('Ответ')
  author_answer = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
    related_name='author_answer',
    verbose_name='Автор ответа'
  )
  attraction = models.ForeignKey(
    Attraction,
    on_delete=models.CASCADE,
    verbose_name='Достопримечательность'
  )
  
  class Meta:
    verbose_name = 'Вопрос/Ответ'
    verbose_name_plural = 'Вопросы/Ответы'
  
  def __str__(self):
    return self.question
