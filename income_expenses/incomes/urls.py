from django.urls import path

from . import views

app_name = 'incomes'

urlpatterns = [
    path('', views.incomes_list, name='incomes_list'),
    path('add/', views.AddIncomeView.as_view(), name='incomes_add'),
    path('<int:pk>/', views.UpdateIncomeView.as_view(), name='incomes_update'),
    path('<int:pk>/delete/', views.DeleteIncomeView.as_view(),
         name='incomes_delete'),
]
