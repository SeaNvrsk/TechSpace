import os
from transliterate import translit
from django.db import models
from django.contrib.auth.models import AbstractUser
from storages.backends.ftp import FTPStorage
from mptt.models import MPTTModel

fs = FTPStorage()


def my_awesome_upload_function(instance, filename):
    filename = translit(filename, reversed=True)
    return os.path.join('media/avatars/{}/'.format(instance.get_directory()), filename)


class User(AbstractUser):
    SIDEBAR_COLOR_CHOICES = (
        ('primary', 'Розовый'),
        ('dark', 'Черный'),
        ('info', 'Голубой'),
        ('success', 'Зеленый'),
        ('warning', 'Оранжевый'),
        ('danger', 'Красный'),
    )

    SIDEBAR_TYPE_CHOICES = (
        ('bg-transparent', 'Прозрачный'),
        ('bg-white', 'Белый')
    )

    NAVBAR_FIXED_CHOICES = (
        ('true', 'Да'),
        ('false', 'Нет')
    )

    avatar = models.FileField(upload_to=my_awesome_upload_function, null=True, blank=True, verbose_name='Ваше фото', storage=fs)
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    location = models.CharField(max_length=30, null=True, blank=True, verbose_name='Страна')
    birth_date = models.DateField(null=True, blank=True, verbose_name='День рождения')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')

    """Поля настройки приложения для каждого пользователя"""
    sidebar_color = models.CharField(max_length=20, null=True, blank=True, default='info',
                                     choices=SIDEBAR_COLOR_CHOICES,
                                     verbose_name='Цвет панели администратора')
    sidebar_type = models.CharField(max_length=20, null=True, blank=True, default='bg-transparent',
                                    choices=SIDEBAR_TYPE_CHOICES,
                                    verbose_name='Тип панели')

    navbar_fixed = models.CharField(max_length=10, null=True, blank=True, default='false',
                                    choices=NAVBAR_FIXED_CHOICES,
                                    verbose_name='navbar закреплен')

    def get_directory(self):
        directory = str.replace(translit(self.get_full_name(), reversed=True), ' ', '_')
        return directory

