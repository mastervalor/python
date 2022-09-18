from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=225)
    desc = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Authors(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    books = models.ManyToManyField(Books, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)