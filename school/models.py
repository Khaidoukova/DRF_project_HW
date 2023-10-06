from datetime import date

from django.conf import settings
from django.db import models
from django.utils import timezone
from users.models import User


from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', blank=True, null=True)
    video_url = models.CharField(max_length=150, verbose_name='ссылка на видео', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='категория', blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

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
    payment_date = models.DateTimeField(default=timezone.now, verbose_name='дата оплаты')
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


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name="Пользователь", )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', null=True, blank=True)

    def __str__(self):
        return f"{self.user} подписан на {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'



