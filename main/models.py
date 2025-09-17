import uuid
from django.db import models

CATEGORY_CHOICES = [
    ("jersey", "Jersey"),
]

SIZE_CHOICES = [
    ("xxs", "XXS"),
    ("xs", "XS"),
    ("s", "S"),
    ("m", "M"),
    ("l", "L"),
    ("xl", "XL"),
    ("xxl", "XXL"),
]

SLEEVE_CHOICES = [
    ("none", "None"),
    ("short", "Short Sleeve"),
    ("long", "Long Sleeve"),
]

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100) 
    price = models.IntegerField()                          
    description = models.TextField()                       
    thumbnail = models.URLField()                         
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="jersey",
    )
    is_featured = models.BooleanField(default=False)      

    #Optionals/tambahan 
    team = models.CharField(max_length=100, blank=True)    
    season = models.CharField(max_length=20, blank=True)   
    size = models.CharField(
            max_length=4,
            choices=SIZE_CHOICES,
            blank=True,  # biar opsional
            null=True,
        )
    sleeve_type = models.CharField(
        max_length=12,
        choices=SLEEVE_CHOICES,
        blank=True,  # biar opsional
        null=True,
    )
    condition = models.CharField(max_length=50, blank=True)    
    manufacturer = models.CharField(max_length=50, blank=True) 
    stock = models.IntegerField(default=0)         
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

