from django.shortcuts import render
from .models import Product   

def show_main(request):
    context = {
        "app_name": "KitKeeper",          
        "student_name": "Nisrina Fatimah",
        "student_class": "PBP F",  
    }
    return render(request, "main.html", context)


