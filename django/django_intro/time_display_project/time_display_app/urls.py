from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('/time_display', views.main)
]