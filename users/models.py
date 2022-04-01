from statistics import mode
from unicodedata import name
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.forms import ImageField
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid

from .managers import CustomUserManager

def user_avatar_path(instance, filename):
    name = uuid.uuid4()
    return 'images/users/avatars/{0}.{1}'.format(name, filename.split('.')[-1])

def user_guide_photo_path(instance, filename):
    name = uuid.uuid4()
    return 'images/users/guides/{0}.{1}'.format(name, filename.split('.')[-1])

def user_guide_certificate_path(instance, filename):
    name = uuid.uuid4()
    return 'images/users/guides/certificates/{0}.{1}'.format(name, filename.split('.')[-1])


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', unique=True)
    is_active = models.BooleanField('Активность', default=True)
    is_superuser = models.BooleanField('Админ', default=False)
    is_staff = models.BooleanField('Сотрудник', default=False)
    is_guide = models.BooleanField('Гид', default=False)
    is_travel_company = models.BooleanField('Туристическая компания', default=False)
    date_created = models.DateTimeField('Дата создания', auto_now_add=timezone.now())
    date_updated = models.DateTimeField('Дата обновления', auto_now=timezone.now())
    name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=10, unique=True, blank=True, null=True)
    nickname = models.CharField('Никнейм', max_length=50, unique=True, blank=True, null=True)
    avatar = ProcessedImageField(upload_to=user_avatar_path, processors=[ResizeToFill(150, 150)], format='JPEG', options={'quality': 80,}, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
    
    
class UserGuide(models.Model):
    about = models.TextField('О гиде', blank=True, null=True)
    count_excursions = models.PositiveSmallIntegerField('Кол-во экскурсий', blank=True, null=True)
    count_guided_tours = models.PositiveIntegerField('Кол-во проведенных экскурсий', blank=True, null=True)
    count_reviews = models.PositiveIntegerField('Кол-во отзывов', blank=True, null=True)
    average_rating = models.FloatField('Средний рейтинг', blank=True, null=True)
    count_articles = models.PositiveIntegerField('Кол-во статей', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    
    class Meta:
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'
    
    def __str__(self):
        return str(self.id)


class UserGuidePhoto(models.Model):
    guide = models.ForeignKey(UserGuide, on_delete=models.CASCADE, verbose_name='Гид')
    photo = models.ImageField(upload_to=user_guide_photo_path)
    small_photo = ProcessedImageField(upload_to=user_guide_photo_path, processors=[ResizeToFill(150, 150)], format='JPEG', options={'quality': 80,})
    description = models.CharField('Описание', max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Фото гида'
        verbose_name_plural = 'Фотографии гидов'
    
    def __str__(self):
        return str(self.id)


class UserGuideCertificate(models.Model):
    certificate = models.ImageField(upload_to=user_guide_certificate_path)
    small_certificate = ProcessedImageField(upload_to=user_guide_certificate_path, processors=[ResizeToFill(150, 150)], format='JPEG', options={'quality': 100,})
    description = models.TextField('Описание', blank=True, null=True)
    guide = models.ForeignKey(UserGuide, on_delete=models.CASCADE, verbose_name='Гид')
    
    class Meta:
        verbose_name = 'Сертификат гида'
        verbose_name_plural = 'Сертификаты гидов'
    
    def __str__(self):
        return str(self.id)

