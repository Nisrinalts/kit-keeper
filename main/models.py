import uuid
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100) 
    price = models.IntegerField()                          
    description = models.TextField()                       
    thumbnail = models.URLField()                         
    category = models.CharField(max_length=50)            
    is_featured = models.BooleanField(default=False)      

    #Optionals/tambahan 
    team = models.CharField(max_length=100, blank=True)    
    season = models.CharField(max_length=20, blank=True)   
    size = models.CharField(max_length=5, blank=True)      
    sleeve_type = models.CharField(max_length=20, blank=True)  
    condition = models.CharField(max_length=50, blank=True)    
    manufacturer = models.CharField(max_length=50, blank=True) 
    stock = models.PositiveIntegerField(default=0)         
    created_at = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.name

