from django.db import models


class CreatedUpdatedModel(models.Model):
    """Abstract model. Adds the created and updated date."""
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
        help_text="Автоматически задается при создании",
    )

    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время изменения",
        help_text="Автоматически задается при изменении",
    )

    class Meta:
        abstract = True


class IsActiveModel(models.Model):
    """Abstract model. Adds is_active field."""
    is_active = models.BooleanField(
        verbose_name='Активность',
        default=True,
    )

    class Meta:
        abstract = True
