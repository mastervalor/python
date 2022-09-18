from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('destroy_session', views.destroy),
    path('double', views.double)
]