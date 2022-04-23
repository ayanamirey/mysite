from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=60, verbose_name='Название продукта')
    text = models.TextField(verbose_name='Описание продукта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['id']