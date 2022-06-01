from django.db import models

from core.models import CreatedUpdatedModel
from companies.models import Company


class Income(CreatedUpdatedModel):
    """Model Income."""
    date = models.DateField(
        verbose_name='Дата',
        help_text='Дата дохода',
    )
    summa = models.DecimalField(
        verbose_name='Сумма',
        help_text='Сумма дохода в рублях',
        max_digits=12,
        decimal_places=2,
    )
    company = models.ForeignKey(
        Company,
        verbose_name='Компания',
        help_text='Контрагент операции',
        related_name='incomes',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'
        ordering = ['date', 'company']

    def __str__(self):
        return f'Доход на сумму {self.summa} от компании {self.company}'
