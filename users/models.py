from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=30, unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)
    country = models.CharField(max_length=20, verbose_name='Город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users', verbose_name='Аватар', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
