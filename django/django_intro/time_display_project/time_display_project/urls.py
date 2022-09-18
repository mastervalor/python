from django.urls import path,include

urlpatterns = [
    path('', include('time_display_app.urls')),
]