from django.urls import path, include
from . import views
from .views import home
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
    # path('', views.index),
    # path('hello/<str:username>', views.hello),
    # path('about/', views.about),
    # path('customers/', views.customers),
    # path('customer/<str:customer_id>', views.customers_by_id),
]