from django.db import models

from admintools.models import CoreModel


class Category(CoreModel):
    title = models.CharField(
        verbose_name='наименование',
        max_length=64
    )
    discount = models.FloatField(
        verbose_name='скидка'
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.id}: {self.title}'


class Product(CoreModel):
    title = models.CharField(
        verbose_name='наименование',
        max_length=128
    )
    description = models.TextField(
        verbose_name='описание'
    )
    image = models.ImageField(
        verbose_name='изображение',
        null=True
    )
    price = models.FloatField(
        verbose_name='цена'
    )
    discount = models.FloatField(
        verbose_name='скидка',
        null=True,
        default=None,
    )
    aviable = models.IntegerField(
        verbose_name='доступно',
        default=0
    )

    category = models.ForeignKey(
        Category,
        verbose_name='подкатегория',
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.id}: {self.title}'
