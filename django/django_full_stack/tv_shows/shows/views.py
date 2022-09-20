from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from .models import Shows

def index(request):
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, "index.html", context)

def show(request, show_id):
    context = {
        'show': Shows.objects.get(id = show_id)
    }
    return render(request, "show.html", context)

def edit(request,show_id):
    context = {
        'show': Shows.objects.get(id = show_id)
    }
    return render(request, "edit.html", context)

def update(request,show_id):
    show = Shows.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['desc']
    show.save()
    return redirect('/')

def delete(request,show_id):
    Shows.objects.get(id=show_id).delete()
    return redirect('/')

def new(request):
    return render(request, "new.html")

def save(request):
    Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], desc=request.POST['desc'])
    return redirect('/')