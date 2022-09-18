from django.shortcuts import render, redirect
from .models import Dojos, Ninjas


def index(request):
    context = {
        'dojos': Dojos.objects.all()
    }
    return render(request, 'index.html', context)

def new_ninja(request):
    Ninjas.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], dojo = request.POST['dojo'])
    return redirect('/')

def new_dojo(request):
    Dojos.objects.create(name=request.POST['name'],state=request.POST['state'], city = request.POST['city'])
    return redirect('/')