# Generated by Django 3.2 on 2022-12-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221116_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок каталог')),
                ('c_body', models.TextField(blank=True, null=True, verbose_name='Текст каталог')),
                ('history_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинки каталог')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='photo_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]