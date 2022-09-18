from django.urls import path
from . import views

urlpatterns = [
    path('/', views.root),
    path('/blogs', views.index),
    path('/blogs/new', views.new),
    path('/blogs/create', views.create),
    path('/blogs/<int:numbers>', views.show),
    path('/blogs/<int:numbers>/edit', views.edit),
    path('/blogs/<int:numbers>/delete', views.destroy),
    path('/blogs/json', views.json)
]