from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Customer
from .forms import CustomerForm
from .models import Breed
from .models import Feeding
from .models import Porcine
from .forms import PorcineForm


def home(request):
    return render(request, 'myapp/index.html')


# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Index</h1>')

# def customers(request):
#     customers_list = list(Customer.objects.values())
#     return JsonResponse(customers_list, safe=False)
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'myapp/customers.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'myapp/customer_form.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'myapp/customer_form.html', {'form': form})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'myapp/customer_confirm_delete.html', {'customer': customer})

def lista_breeds(request):
    breeds = Breed.objects.all()
    return render(request, 'myapp/breeds.html', {'breeds': breeds})

def lista_feedings(request):
    feedings = Feeding.objects.all()
    return render(request, 'myapp/feedings.html', {'feedings': feedings})

def porcine_list(request):
    porcines = Porcine.objects.all()
    return render(request, 'myapp/porcines.html', {'porcines': porcines})

def add_porcine(request):
    if request.method == 'POST':
        form = PorcineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('porcine_list')
    else:
        form = PorcineForm()
    return render(request, 'myapp/porcine_form.html', {'form': form})

def edit_porcine(request, pk):
    porcine = get_object_or_404(Porcine, pk=pk)
    if request.method == 'POST':
        form = PorcineForm(request.POST, instance=porcine)
        if form.is_valid():
            form.save()
            return redirect('porcine_list')
    else:
        form = PorcineForm(instance=porcine)
    return render(request, 'myapp/porcine_form.html', {'form': form})

def delete_porcine(request, pk):
    porcine = get_object_or_404(Porcine, pk=pk)
    if request.method == 'POST':
        porcine.delete()
        return redirect('porcine_list')
    return render(request, 'myapp/porcine_confirm_delete.html', {'porcine': porcine})

# def customers_by_id(request, customer_id):
#     customer = get_object_or_404(Customer, id_customer=customer_id)
#     return HttpResponse('customer: %s' % customer.first_name)


# def hello(request, username):
#      return HttpResponse('<h1>Hello %s </h1>' % username)


# def about(request):
#     return HttpResponse('<h1>About</h1>')
