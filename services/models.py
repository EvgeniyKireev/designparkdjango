from django.conf import settings
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        indexes = [
            models.Index(fields=['id', 'title', 'slug']),
        ]
    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, db_index=True)
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title
