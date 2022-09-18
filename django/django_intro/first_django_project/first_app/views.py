from django.shortcuts import render, redirect, HttpResponse, JsonResponse


def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('Placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request,numbers):
    return HttpResponse(f'Placeholder to display blog number: {numbers}')

def edit(request,numbers):
    return HttpResponse(f'Placeholder to edit blog: {numbers}')

def destroy(request):
    return redirect('/blogs')

def json(request):
    context = {
        'title': "My first blog",
        'content': "efpkwehfiuwehgfiwgefibweifbwehfbwehfjwbfjkwfbjkwfh"
    }
    return JsonResponse({"title": context['title'], "content": context['content']})