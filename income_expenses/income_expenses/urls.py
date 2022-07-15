from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainpage.urls', namespace='mainpage')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('companies/', include('companies.urls', namespace='companies')),
    path('expenses/', include('expenses.urls', namespace='expenses')),
    path('incomes/', include('incomes.urls', namespace='incomes')),
]

