from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from main.models import Product
from main.forms import ProductForm

import datetime
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import Http404

@login_required(login_url='/login')
def show_main(request):
    tab = request.GET.get("tab", "all")
    qs = Product.objects.all().order_by("-pk")
    if tab == "mine" and request.user.is_authenticated:
        qs = qs.filter(user=request.user)

    context = {
        "products": qs,
        "active_tab": "mine" if tab == "mine" else "all",
        "last_login": request.COOKIES.get("last_login") or request.session.get("last_login"),
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user  
        product.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)  
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, id):
    try:
        product_item = Product.objects.get(pk=id)     
        json_data = serializers.serialize("json", [product_item]) 
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
        else:
            messages.error(request, "Please fix the errors below.")
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # set cookie last_login (dipakai di tugas 4 poin cookies)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    # hapus cookie last_login 
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response

@login_required
def edit_product(request, id):
    # 1) Ambil objek (id kamu bertipe UUID, URL pattern sudah <uuid:id>)
    product = get_object_or_404(Product, pk=id)

    # 2) Guard data legacy: kalau belum punya owner, tolak dan beri info
    if product.user_id is None:
        messages.error(request, "Produk ini belum memiliki owner. Atur owner terlebih dahulu.")
        return redirect("main:show_main")

    # 3) Hanya owner (atau superuser) yang boleh edit
    if product.user_id != request.user.id and not request.user.is_superuser:
        # Samarkan resource dengan 404
        raise Http404("Product not found")

    # 4) Proses form
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil diperbarui.")
            return redirect("main:show_main")
    else:
        form = ProductForm(instance=product)

    return render(request, "edit_product.html", {"form": form, "product": product})

@login_required
def delete_product(request, id):
    # Ambil objeknya dulu
    product = get_object_or_404(Product, pk=id)

    # Hanya proses jika POST (button submit)
    if request.method != "POST":
        return redirect("main:show_main")

    # Kalau product belum punya owner (legacy data), jangan izinkan hapus
    if product.user_id is None:
        messages.error(request, "Produk ini belum memiliki owner. Hubungi admin atau ubah owner dulu.")
        return redirect("main:show_main")

    # Owner check: hanya pemilik (atau superuser) yang boleh
    if product.user_id != request.user.id and not request.user.is_superuser:
        # samarkan dengan 404 agar endpoint tidak dapat dipetakan oleh user lain
        raise Http404("Product not found")

    # Lolos semua check -> hapus
    product.delete()
    messages.success(request, "Produk berhasil dihapus.")
    return redirect("main:show_main")