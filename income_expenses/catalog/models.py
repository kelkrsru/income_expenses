from django.db import models

from core.models import CreatedUpdatedModel, IsActiveModel


class GroupProduct(CreatedUpdatedModel):
    """Model Group for product."""
    name = models.CharField(
        verbose_name='Наименование',
        help_text='Наименование группы продукта/услуги в каталоге',
        max_length=100
    )

    class Meta:
        verbose_name = 'Группа продукта/услуги'
        verbose_name_plural = 'Группы продукта/услуги'
        ordering = ['name']

    def __str__(self):
        return self.name


class Unit(CreatedUpdatedModel):
    """Model Unit."""
    name = models.CharField(
        verbose_name='Наименование',
        help_text='Наименование единицы измерения',
        max_length=50
    )
    short_name = models.CharField(
        verbose_name='Сокращенное наименование',
        help_text='Сокращенное наименование единицы измерения',
        max_length=10
    )
    code = models.CharField(
        verbose_name='Код',
        help_text='Код единицы измерения (напр. PCE - штука, MIN - минута)',
        max_length=10
    )

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        ordering = ['name']

    def __str__(self):
        return self.short_name


class Product(CreatedUpdatedModel, IsActiveModel):
    """Model Product."""
    name = models.CharField(
        verbose_name='Наименование',
        help_text='Наименование продукта/услуги в каталоге',
        max_length=255
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание продукта/услуги в каталоге',
        blank=True,
    )
    group = models.ManyToManyField(
        GroupProduct,
        verbose_name='Группы',
        help_text='Группы продукта/услуги в каталоге',
        related_name='products',
        blank=True,
    )
    unit = models.ForeignKey(
        Unit,
        verbose_name='Единица измерения',
        help_text='Единица измерения продукта/услуги в каталоге',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
    )
    price = models.DecimalField(
        verbose_name='Цена',
        help_text='Розничная цена по каталогу',
        max_digits=12,
        decimal_places=2,
        blank=True,
    )

    class Meta:
        verbose_name = 'Продукт/услуга каталога'
        verbose_name_plural = 'Продукты/услуги каталога'
        ordering = ['name']

    def __str__(self):
        return self.name
