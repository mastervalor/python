from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show/show/<int:id>', views.show),
    path('show/edit/<int:id>',views.edit),
    path('show/delete/<int:id>', views.delete),
    path('show/new', views.new),
    path('show/create', views.save),
    path('show/update/<int:id>', views.update)
]