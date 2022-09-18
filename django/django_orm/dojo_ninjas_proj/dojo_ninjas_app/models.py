from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Ninjas(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    dojo = models.ForeignKey(Dojos, related_name='ninjas',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
