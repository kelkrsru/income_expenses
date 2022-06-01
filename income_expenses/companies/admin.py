from django.contrib import admin

from .models import Company, CompanyType, Requisites


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_my_company',
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyType)
admin.site.register(Requisites)

