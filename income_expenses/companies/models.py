from django.db import models

from core.models import CreatedUpdatedModel


class CompanyType(CreatedUpdatedModel):
    """Model Type Company."""
    name = models.CharField(
        verbose_name='Наименование',
        help_text='Наименование типа компании (напр. Поставщик, Клиент '
                  'и т.п.)',
        max_length=50,
    )

    class Meta:
        verbose_name = 'Тип компании'
        verbose_name_plural = 'Типы компаний'
        ordering = ['name']

    def __str__(self):
        return self.name


class Requisites(CreatedUpdatedModel):
    """Model Requisites Company."""
    inn = models.CharField(
        verbose_name='ИНН',
        help_text='Индивидуальный номер налогоплательщика компании',
        max_length=12,
        unique=True,
    )
    kpp = models.CharField(
        verbose_name='КПП',
        help_text='Код причины постановки',
        max_length=10,
        blank=True,
    )
    ogrn = models.CharField(
        verbose_name='ОГРН/ОГРНИП',
        help_text='Основной государственный регистрационный номер компании',
        max_length=15,
        unique=True,
    )
    short_name = models.CharField(
        verbose_name='Краткое наименование организации',
        help_text='Краткое наименование организации (напр. ООО "УП", '
                  'ИП "Петров И.И.")',
        max_length=255,
    )
    full_name = models.CharField(
        verbose_name='Полное наименование организации',
        help_text='Полное наименование организации (напр. Общество с '
                  'ограниченной ответственностью "Универсальное предприятие", '
                  'Индивидуальный предприниматель "Петров И.И.")',
        max_length=255,
    )
    date_reg = models.DateField(
        verbose_name='Дата государственной регистрации',
        help_text='Дата государственной регистрации компании',
    )
    position_director = models.CharField(
        verbose_name='Должность руководителя',
        help_text='Наименование должности руководителя компании (напр. '
                  'Директор, Генеральный директор и т.п.',
        default='Директор',
        max_length=50,
        blank=True,
    )
    name_director = models.CharField(
        verbose_name='Руководитель',
        help_text='Фамилия, имя, отчество руководителя компании',
        max_length=255,
    )
    legal_address = models.CharField(
        verbose_name='Юридический адрес',
        help_text='Юридический адрес компании',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'
        ordering = ['inn']

    def __str__(self):
        return self.inn


class Company(CreatedUpdatedModel):
    """Model Company."""
    name = models.CharField(
        verbose_name='Наименование компании',
        help_text='Наименование компании в системе (может отличаться от '
                  'официального наименования компании',
        max_length=255,
    )
    is_my_company = models.BooleanField(
        verbose_name='Моя компания',
        help_text='Признак компании, по которой ведется учет',
        default=False,
    )
    phone = models.CharField(
        verbose_name='Телефон',
        help_text='Основной телефон компании',
        max_length=20,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Основная электронная почта компании',
        blank=True,
    )
    site = models.URLField(
        verbose_name='Сайт',
        help_text='Сайт компании',
        blank=True,
    )
    type = models.ForeignKey(
        CompanyType,
        verbose_name='Тип',
        help_text='Тип компании',
        related_name='companies',
        on_delete=models.SET_NULL,
        null=True,
    )
    requisites = models.OneToOneField(
        Requisites,
        verbose_name='Реквизиты',
        help_text='Реквизиты компании',
        related_name='company',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name']

    def __str__(self):
        return self.name
