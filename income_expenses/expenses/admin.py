from django.contrib import admin

from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'summa',
        'company',
    )


admin.site.register(Expense, ExpenseAdmin)
