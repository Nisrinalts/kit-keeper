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

from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.utils import timezone

@login_required(login_url='/login')
def show_main(request):
    tab = request.GET.get("tab", "all")
    context = {
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
        messages.success(request, "Product created!")
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
    product_list = Product.objects.all()
    data = [
        {
            "id": str(p.id),
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "thumbnail": p.thumbnail,          
            "category": p.category,            
            "is_featured": p.is_featured,
            "team": p.team,
            "season": p.season,
            "size": p.size,                   
            "sleeve_type": p.sleeve_type,     
            "condition": p.condition,
            "manufacturer": p.manufacturer,
            "stock": p.stock,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "user_id": p.user_id,             
        }
        for p in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)  
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'team': product.team,
            'season': product.season,
            'size': product.size,
            'sleeve_type': product.sleeve_type,
            'condition': product.condition,
            'manufacturer': product.manufacturer,
            'stock': product.stock,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
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
    messages.success(request, "Logged out successfully.")
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

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    if not request.user.is_authenticated:
         return JsonResponse({"detail": "Unauthorized"}, status=401)

    # Ambil & sanitize
    name         = strip_tags(request.POST.get("name", "").strip())
    description  = strip_tags(request.POST.get("description", "")) if request.POST.get("description") is not None else ""
    category     = request.POST.get("category") or "jersey"
    thumbnail    = request.POST.get("thumbnail") or ""
    is_featured  = (request.POST.get("is_featured") == "on")
    team         = strip_tags(request.POST.get("team", "")) if request.POST.get("team") is not None else ""
    season       = strip_tags(request.POST.get("season", "")) if request.POST.get("season") is not None else ""
    size         = request.POST.get("size") or None
    sleeve_type  = request.POST.get("sleeve_type") or None
    condition    = strip_tags(request.POST.get("condition", "")) if request.POST.get("condition") is not None else ""
    manufacturer = strip_tags(request.POST.get("manufacturer", "")) if request.POST.get("manufacturer") is not None else ""

    # Angka
    try:
        price = int(request.POST.get("price") or 0)
        stock = int(request.POST.get("stock") or 0)
    except ValueError:
        return JsonResponse({"detail": "price/stock harus berupa angka."}, status=400)

    if not name:
        return JsonResponse({"detail": "Name wajib diisi."}, status=400)

    try:
        p = Product.objects.create(
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            team=team,
            season=season,
            size=size if size else None,
            sleeve_type=sleeve_type if sleeve_type else None,
            condition=condition,
            manufacturer=manufacturer,
            stock=stock,
            user=request.user if request.user.is_authenticated else None,
        )
    except Exception as e:
        return JsonResponse({"detail": f"invalid payload: {e}"}, status=400)

    return JsonResponse({"detail": "CREATED", "id": str(p.id)}, status=201)



@require_POST
def update_product_entry_ajax(request, id):
    # Ambil product (id bertipe UUID di urls)
    product = get_object_or_404(Product, pk=id)

    # Guard legacy: wajib punya owner dahulu
    if product.user_id is None:
        return JsonResponse({"detail": "Produk belum memiliki owner. Atur owner terlebih dahulu."}, status=400)

    # Hanya owner / superuser
    if product.user_id != (request.user.id if request.user.is_authenticated else None) and not request.user.is_superuser:
        return JsonResponse({"detail": "Product not found."}, status=404)  # samarkan resource

    # Ambil payload
    name         = strip_tags(request.POST.get("name", "")) or product.name
    description  = strip_tags(request.POST.get("description", "")) if request.POST.get("description") is not None else product.description
    category     = request.POST.get("category") if request.POST.get("category") is not None else product.category
    thumbnail    = request.POST.get("thumbnail") if request.POST.get("thumbnail") is not None else product.thumbnail
    is_featured  = (request.POST.get("is_featured") == 'on') if request.POST.get("is_featured") is not None else product.is_featured
    team         = strip_tags(request.POST.get("team", "")) if request.POST.get("team") is not None else product.team
    season       = strip_tags(request.POST.get("season", "")) if request.POST.get("season") is not None else product.season
    size         = request.POST.get("size") if request.POST.get("size") is not None else product.size
    sleeve_type  = request.POST.get("sleeve_type") if request.POST.get("sleeve_type") is not None else product.sleeve_type
    condition    = strip_tags(request.POST.get("condition", "")) if request.POST.get("condition") is not None else product.condition
    manufacturer = strip_tags(request.POST.get("manufacturer", "")) if request.POST.get("manufacturer") is not None else product.manufacturer

    price_raw = request.POST.get("price")
    stock_raw = request.POST.get("stock")
    try:
        if price_raw is not None:
            product.price = int(price_raw or 0)
        if stock_raw is not None:
            product.stock = int(stock_raw or 0)
    except ValueError:
        return JsonResponse({"detail": "price/stock harus berupa angka."}, status=400)

    # Set nilai lain
    product.name = name
    product.description = description
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.team = team
    product.season = season
    product.size = size if size else None
    product.sleeve_type = sleeve_type if sleeve_type else None
    product.condition = condition
    product.manufacturer = manufacturer

    # Simpan
    product.save()

    # Balikkan JSON ringkas (bisa dipakai buat update UI kalau mau)
    return JsonResponse({
        "id": str(product.id),
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "thumbnail": product.thumbnail,
        "category": product.category,
        "is_featured": product.is_featured,
        "team": product.team,
        "season": product.season,
        "size": product.size,
        "sleeve_type": product.sleeve_type,
        "condition": product.condition,
        "manufacturer": product.manufacturer,
        "stock": product.stock,
        "user_id": product.user_id,
    }, status=200)


@csrf_exempt
@require_POST
def delete_product_entry_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    # Legacy guard
    if product.user_id is None:
        return JsonResponse({"detail": "Produk belum memiliki owner. Hubungi admin/atur owner dulu."}, status=400)

    # Hanya owner atau superuser
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Product not found."}, status=404)

    if product.user_id != request.user.id and not request.user.is_superuser:
        return JsonResponse({"detail": "Product not found."}, status=404)

    product.delete()
    return JsonResponse({"detail": "DELETED"}, status=200)


@csrf_exempt
@require_POST
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if not form.is_valid():
        return JsonResponse({"detail": "Invalid username or password."}, status=400)

    user = form.get_user()
    login(request, user)

    # set cookie last_login 
    response = JsonResponse(
        {
            "detail": "LOGGED_IN",
            "redirect": reverse("main:show_main"),
        },
        status=200,
    )
    # cookie + session (biar konsisten dua-duanya)
    response.set_cookie("last_login", str(datetime.datetime.now()))
    request.session["last_login"] = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    return response


@csrf_exempt
@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)

    form.save()  
    # arahkan user ke halaman login
    return JsonResponse(
        {
            "detail": "REGISTERED",
            "redirect": reverse("main:login"),
        },
        status=201,
    )

@csrf_exempt
@require_POST
def logout_ajax(request):
    logout(request)
    response = JsonResponse(
        {
            "detail": "LOGGED_OUT",
            "redirect": reverse("main:login"),
        },
        status=200,
    )
    response.delete_cookie("last_login")
    return response
