from django.contrib import admin

from .models import Income


class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'summa',
        'company',
    )


admin.site.register(Income, IncomeAdmin)
