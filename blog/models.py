from django.db import models
from django.forms import ValidationError
from django.utils import timezone

from users.models import User


class Category(models.Model):
  name = models.CharField('Название', max_length=255, unique=True)
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=True)
  count_articles = models.PositiveSmallIntegerField('Кол-во статей', default=0)
  title = models.CharField('Title', max_length=100)
  description = models.CharField('Description', max_length=255)
  keywords = models.CharField('Keywords', max_length=255)
  text = models.TextField('Текст раздела', blank=True)
  parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
  depth = models.PositiveSmallIntegerField('Уровень вложенности')
  
  class Meta:
    db_table = 'blog_category'
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'
  
  def __str__(self):
    return self.name


def validate_name(value):
  category = Category.objects.filter(name=value).first()
  if category is not None:
    str = 'Тег с названием «{0}» не может быть добавлен (название «{0}» используется в категориях)'
    raise ValidationError(str.format(value))

class Tag(models.Model):
  STATUS_CHOICES = [
    ('MO', 'Модерация'),
    ('PU', 'Опубликован'),
    ('RE', 'Удален'),
  ]
  name = models.CharField('Название', max_length=255, unique=True, validators=[validate_name])
  url = models.CharField('URL', max_length=255, unique=True)
  is_active = models.BooleanField('Активность', default=False)
  count_articles = models.PositiveIntegerField('Кол-во статей', blank=True, null=True)
  date_created = models.DateTimeField('Дата создания', auto_now_add=timezone.now())
  status = models.CharField('Статус', max_length=2, choices=STATUS_CHOICES, default='MO')
  
  class Meta:
    db_table = 'blog_tag'
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'
  
  def __str__(self):
    return self.name


class PopularTag(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
  
  class Meta:
    db_table = 'blog_popular_tag'
    verbose_name = 'Популярный тег'
    verbose_name_plural = 'Популярные теги'


class Article(models.Model):
  name = models.CharField('Название', max_length=255)
  url = models.CharField('URL', max_length=255)
  is_active = models.BooleanField('Активность', default=False)
  date_created = models.DateField('Дата создания', auto_now_add=True)
  date_published = models.DateField('Дата публикации')
  preview_text = models.TextField('Превью текст')
  detail_text = models.TextField('Текст статьи')
  category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
  author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Автор')
  tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
  count_comments = models.PositiveIntegerField('Кол-во комментариев', default=0)
  average_rating = models.PositiveIntegerField('Рейтинг', blank=True, null=True)
  # preview_image
  # detail_image
  
  class Meta:
    db_table = 'blog_acticle'
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'
  
  def __str__(self):
    return self.name


class Comment(models.Model):
  STATUS_CHOICES = [
    ('MO', 'Модерация'),
    ('PU', 'Опубликован'),
    ('RE', 'Удален'),
  ]
  author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Автор комментария')
  article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
  date_created = models.DateTimeField('Дата создания', auto_now_add=True)
  comment = models.TextField('Комментарий')
  is_active = models.BooleanField('Активность', default=True)
  status = models.CharField('Статус', max_length=2, choices=STATUS_CHOICES, default='MO')
  rating = models.PositiveSmallIntegerField('Рейтинг')
  
  class Meta:
    db_table = 'blog_comment'
    verbose_name = 'Комментарий'
    verbose_name_plural = 'Комментарии'
