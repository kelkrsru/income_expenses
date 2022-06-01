from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls', namespace='mainpage')),
    path('companies/', include('companies.urls', namespace='companies')),
    path('incomes/', include('incomes.urls', namespace='incomes')),
]
