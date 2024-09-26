from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    # Redirigir la página raíz al panel de administración
    path('', lambda request: redirect('customers/', permanent=True)),

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),
    
    path('breeds/', views.breed_list, name='breed_list'),
    path('breeds/add/', views.add_breed, name='add_breed'),
    path('breeds/edit/<int:pk>/', views.edit_breed, name='edit_breed'),
    path('breeds/delete/<int:pk>/', views.delete_breed, name='delete_breed'),
    
    path('feedings/', views.feeding_list, name='feeding_list'),
    path('feedings/add/', views.add_feeding, name='add_feeding'),
    path('feedings/edit/<int:pk>/', views.edit_feeding, name='edit_feeding'),
    path('feedings/delete/<int:pk>/', views.delete_feeding, name='delete_feeding'),
    
    path('porcines/', views.porcine_list, name='porcine_list'),
    path('porcines/add/', views.add_porcine, name='add_porcine'),
    path('porcines/edit/<int:pk>/', views.edit_porcine, name='edit_porcine'),
    path('porcines/delete/<int:pk>/', views.delete_porcine, name='delete_porcine'),

    path('summary/', views.customer_porcine_summary, name='customer_porcine_summary'),
]