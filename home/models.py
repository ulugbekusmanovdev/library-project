from django.db import models

# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'


class Library(models.Model):
    l_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок о библиотеке')
    l_body = models.TextField(blank=True, null=True, verbose_name='Текст о библиотеке')
    m_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок миссия')
    m_body = models.TextField(blank=True, null=True, verbose_name='Текст миссия')
    os_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок основные зад')
    os_body = models.TextField(blank=True, null=True, verbose_name='Текст основные зад')
    history_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок история')
    history_body = models.TextField(blank=True, null=True, verbose_name='Текст история')
    history_image = models.ImageField(blank=True, null=True, verbose_name='Картинки история')


    class Meta:
        verbose_name = 'О Библиотеке'
        verbose_name_plural = 'О Библиотеке'

