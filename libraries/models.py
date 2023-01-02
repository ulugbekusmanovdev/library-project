from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультет"


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Библотекар"
        verbose_name_plural = "Библотекар"


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='book/pdfs/')
    photo = models.ImageField(upload_to='book/photos/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книги"
        verbose_name_plural = "Книги"


class Chat(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)
    # image = models.ImageField(upload_to='book/photos/', blank=True, null=True)

    def __str__(self):
        return self.customer


