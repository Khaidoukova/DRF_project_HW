from datetime import date

from django.db import models
from django.utils import timezone

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', blank=True, null=True)
    video_url = models.URLField(max_length=150, verbose_name='ссылка на видео', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='категория', blank=True, null=True)

    def __str__(self):
        return f'{self.title} (курс {self.course})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    PAYMENT_CHOICES = [
        ("cash", "наличные"),
        ("transfer", "перевод"),
]

    user = models.CharField(max_length=50,  verbose_name='пользователь', blank=True, null=True)
    payment_date = models.DateField(default=date.today(), verbose_name='дата оплаты')
    payed_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', blank=True, null=True)
    payed_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', blank=True, null=True)
    amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=15, default='перевод', choices=PAYMENT_CHOICES, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} ({self.payed_course if self.payed_course else self.payed_lesson} - {self.payment_date})'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('-payment_date',)