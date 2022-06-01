from django.urls import path

from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.companies_list, name='companies_list'),
    path('add/', views.company_add, name='company_add'),
    path('<int:pk>/', views.company_update, name='company_update'),
    path('company_type/', views.company_type_list, name='company_type_list'),
    path('company_type/add/', views.AddCompanyTypeView.as_view(), name='add_company_type'),
    path('company_type/<int:pk>/', views.UpdateCompanyTypeView.as_view(), name='update_company_type'),
    path('company_type/<int:pk>/delete/', views.DeleteCompanyTypeView.as_view(), name='delete_company_type'),
    path('add/find_by_inn/', views.find_by_inn, name='find_by_inn'),
]