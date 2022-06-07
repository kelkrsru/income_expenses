from django.db import models

from core.models import CreatedUpdatedModel
from companies.models import Company


class Expense(CreatedUpdatedModel):
    """Model Expense."""
    date = models.DateField(
        verbose_name='Дата',
        help_text='Дата расхода',
    )
    summa = models.DecimalField(
        verbose_name='Сумма',
        help_text='Сумма расхода в рублях',
        max_digits=12,
        decimal_places=2,
    )
    company = models.ForeignKey(
        Company,
        verbose_name='Компания',
        help_text='Контрагент операции',
        related_name='expenses',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
        ordering = ['date', 'company']

    def __str__(self):
        return f'Расход на сумму {self.summa} по компании {self.company}'
