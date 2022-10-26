from django.db import models

# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')


class Library(models.Model):
    l_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    l_body = models.TextField(blank=True, null=True, verbose_name='Текст')
    m_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    m_body = models.TextField(blank=True, null=True, verbose_name='Текст')
    os_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    os_body = models.TextField(blank=True, null=True, verbose_name='Текст')
    history_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    history_body = models.TextField(blank=True, null=True, verbose_name='Текст')
    history_image = models.ImageField(blank=True, null=True, verbose_name='Картинки')


    class Meta:
        verbose_name = 'О Библиотеке'
        verbose_name_plural = 'О Библиотеке'
