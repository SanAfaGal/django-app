from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Customer
from .models import Breed
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'myapp/index.html')


# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Index</h1>')

# def customers(request):
#     customers_list = list(Customer.objects.values())
#     return JsonResponse(customers_list, safe=False)
def lista_customers(request):
    customers = Customer.objects.all()
    return render(request, 'myapp/customers.html', {'customers': customers})

def lista_breeds(request):
    breeds = Breed.objects.all()
    return render(request, 'myapp/breeds.html', {'breeds': breeds})

# def customers_by_id(request, customer_id):
#     customer = get_object_or_404(Customer, id_customer=customer_id)
#     return HttpResponse('customer: %s' % customer.first_name)


# def hello(request, username):
#      return HttpResponse('<h1>Hello %s </h1>' % username)


# def about(request):
#     return HttpResponse('<h1>About</h1>')
