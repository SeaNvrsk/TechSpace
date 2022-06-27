from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='Ваше фото')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    location = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')
    birth_date = models.DateField(null=True, blank=True, verbose_name='День рождения')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')