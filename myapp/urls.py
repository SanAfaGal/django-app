from django.urls import path, include
from . import views
from .views import home
from .views import customer_list
from .views import lista_breeds
from .views import lista_feedings
from .views import porcine_list
from django.contrib import admin

# urlpatterns = [
#     path('', home, name='home'),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('myapp.urls')),
# ]
urlpatterns = [
    path("home/", views.home),
    path('customers/', customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:pk>/', views.delete_customer, name='delete_customer'),
    
    path('breeds/', lista_breeds, name='lista_breeds'),
    path('feedings/', lista_feedings, name='lista_feedings'),
    
    path('porcines/', views.porcine_list, name='porcine_list'),
    path('porcines/add/', views.add_porcine, name='add_porcine'),
    path('porcines/edit/<int:pk>/', views.edit_porcine, name='edit_porcine'),
    path('porcines/delete/<int:pk>/', views.delete_porcine, name='delete_porcine'),
    # path('', views.index),
    # path('hello/<str:username>', views.hello),
    # path('about/', views.about),
    # path('customers/', views.customers),
    # path('customer/<str:customer_id>', views.customers_by_id),
]