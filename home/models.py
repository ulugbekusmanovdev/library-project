from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField


# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Текст')
    ads_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


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


class Photo(models.Model):
    image = models.ImageField(blank=True, null=True, verbose_name='Картинки')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    photo_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Photo, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='img/')


class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']


class Catalog(models.Model):
    c_title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок каталог')
    c_body = RichTextField(blank=True, null=True, verbose_name='Текст каталог')
    c_image = models.ImageField(blank=True, null=True, verbose_name='Картинки каталог')

    def __str__(self):
        return str(self.c_title)

    class Meta:
        verbose_name = 'Каталоги'
        verbose_name_plural = 'Каталоги'


class Readers(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, )
    text = RichTextField(blank=True, null=True, verbose_name="Текст")
    image = models.ImageField(blank=True, null=True, verbose_name='Картинки')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Читателям'
        verbose_name_plural = 'Читателям'


class Newspaper(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Газета'
        verbose_name_plural = 'Газета'
        ordering = ('id',)


class Journal(models.Model):
    number = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журнал'
        ordering = ('id',)


class Contact(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(blank=True, null=False, verbose_name="Текст")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Как связаться'
        verbose_name_plural = 'Как связаться'
