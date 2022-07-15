from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path(r'', views.ListProductsView.as_view(), name='products_list'),
    path('add/', views.AddProductView.as_view(), name='product_add'),
    path('<int:pk>/', views.UpdateProductView.as_view(),
         name='product_update'),
    path('<int:pk>/delete/', views.DeleteProductView.as_view(),
         name='product_delete'),
    path('units/', views.ListUnitView.as_view(), name='units_list'),
    path('units/add/', views.AddUnitView.as_view(), name='unit_add'),
    path('units/<int:pk>/', views.UpdateUnitView.as_view(),
         name='unit_update'),
    path('units/<int:pk>/delete/', views.DeleteUnitView.as_view(),
         name='unit_delete'),
    path('groups/', views.ListGroupsView.as_view(), name='groups_list'),
    path('groups/add/', views.AddGroupView.as_view(), name='group_add'),
    path('groups/<int:pk>/', views.UpdateGroupView.as_view(),
         name='group_update'),
    path('groups/<int:pk>/delete/', views.DeleteGroupView.as_view(),
         name='group_delete'),
]
