from django.urls import path, include
from . import views
from .views import home
from .views import lista_customers
from .views import lista_breeds
from .views import lista_feedings
from .views import lista_porcines
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
    path('customers/', lista_customers, name='lista_customers'),
    path('breeds/', lista_breeds, name='lista_breeds'),
    path('feedings/', lista_feedings, name='lista_feedings'),
    path('porcines/', lista_porcines, name='lista_porcines'),
    # path('', views.index),
    # path('hello/<str:username>', views.hello),
    # path('about/', views.about),
    # path('customers/', views.customers),
    # path('customer/<str:customer_id>', views.customers_by_id),
]