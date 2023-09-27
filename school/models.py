from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='course/', verbose_name='Превью', blank=True, null=True)
    url = models.URLField(max_length=150, verbose_name='ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='категория', blank=True, null=True)

    def __str__(self):
        return f'{self.title} (курс {self.course})'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'



