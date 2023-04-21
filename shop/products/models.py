from django.db import models

from admintools.models import CoreModel


class Category(CoreModel):
    title = models.CharField(
        verbose_name='наименование',
        max_length=64,
        db_index=True,
    )
    discount = models.FloatField(
        verbose_name='скидка',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'id:{self.id} {self.title}'


class Product(CoreModel):
    title = models.CharField(
        verbose_name='наименование',
        max_length=128,
        db_index=True
    )
    description = models.TextField(
        verbose_name='описание'
    )
    image = models.ImageField(
        verbose_name='изображение',
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=10,
        decimal_places=2,
    )
    discount = models.FloatField(
        verbose_name='скидка',
        blank=True,
        null=True,
        default=None,
    )
    stock = models.IntegerField(
        verbose_name='доступно',
        default=0
    )

    category = models.ForeignKey(
        Category,
        verbose_name='подкатегория',
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'id:{self.id} {self.title}'


# class Cart(CoreModel):
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE
#     )
