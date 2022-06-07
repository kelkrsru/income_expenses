from django.urls import path

from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.expenses_list, name='expenses_list'),
    path('add/', views.AddExpenseView.as_view(), name='expenses_add'),
    path('<int:pk>/', views.UpdateExpenseView.as_view(), name='expenses_update'),
    path('<int:pk>/delete/', views.DeleteExpenseView.as_view(), name='expenses_delete'),
]