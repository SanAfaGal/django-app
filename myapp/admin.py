from django.contrib import admin
from .models import Breed, Customer, Feeding, Porcine

# Registrar los modelos para que sean visibles en la interfaz de administración
admin.site.register(Breed)
admin.site.register(Customer)
admin.site.register(Feeding)
admin.site.register(Porcine)
