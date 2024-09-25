from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Customer
from .forms import CustomerForm
from .models import Breed
from .forms import BreedForm
from .models import Feeding
from .forms import FeedingForm
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


def breed_list(request):
    breeds = Breed.objects.all()
    return render(request, 'myapp/breeds.html', {'breeds': breeds})

def add_breed(request):
    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('breed_list')
    else:
        form = BreedForm()
    return render(request, 'myapp/breed_form.html', {'form': form})

def edit_breed(request, pk):
    breed = get_object_or_404(Breed, pk=pk)
    if request.method == 'POST':
        form = BreedForm(request.POST, instance=breed)
        if form.is_valid():
            form.save()
            return redirect('breed_list')
    else:
        form = BreedForm(instance=breed)
    return render(request, 'myapp/breed_form.html', {'form': form})

def delete_breed(request, pk):
    breed = get_object_or_404(Breed, pk=pk)
    if request.method == 'POST':
        breed.delete()
        return redirect('breed_list')
    return render(request, 'myapp/breed_confirm_delete.html', {'breed': breed})


def feeding_list(request):
    feedings = Feeding.objects.all()
    return render(request, 'myapp/feedings.html', {'feedings': feedings})

def add_feeding(request):
    if request.method == 'POST':
        form = FeedingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feeding_list')
    else:
        form = FeedingForm()
    return render(request, 'myapp/feeding_form.html', {'form': form})

def edit_feeding(request, pk):
    feeding = get_object_or_404(Feeding, pk=pk)
    if request.method == 'POST':
        form = FeedingForm(request.POST, instance=feeding)
        if form.is_valid():
            form.save()
            return redirect('feeding_list')
    else:
        form = FeedingForm(instance=feeding)
    return render(request, 'myapp/feeding_form.html', {'form': form})

def delete_feeding(request, pk):
    feeding = get_object_or_404(Feeding, pk=pk)
    if request.method == 'POST':
        feeding.delete()
        return redirect('feeding_list')
    return render(request, 'myapp/feeding_confirm_delete.html', {'feeding': feeding})


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

def customer_porcine_summary(request):
    customers = Customer.objects.all().prefetch_related('porcine_set__breed', 'porcine_set__feeding')
    return render(request, 'myapp/customer_porcine_summary.html', {'customers': customers})

# def hello(request, username):
#      return HttpResponse('<h1>Hello %s </h1>' % username)


# def about(request):
#     return HttpResponse('<h1>About</h1>')
