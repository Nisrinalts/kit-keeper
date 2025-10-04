from django.urls import path
from main.views import register
from main.views import login_user
from main.views import logout_user 
from main.views import (
    show_main, create_product, show_product,
    show_xml, show_json, show_xml_by_id, show_json_by_id, edit_product, delete_product, update_product_entry_ajax, delete_product_entry_ajax,
    login_ajax, register_ajax, logout_ajax,
)
from .views import add_product_entry_ajax


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path("add/", create_product, name="create_product"),
    path("detail/<str:id>/", show_product, name="show_product"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<str:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:product_id>/", show_json_by_id, name="show_json_by_id"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("product/<uuid:id>/edit/", edit_product, name="edit_product"),
    path("product/<uuid:id>/delete/", delete_product, name="delete_product"),
    path("create-product-ajax", add_product_entry_ajax, name="add_product_entry_ajax"),
    path("product/<uuid:id>/update-ajax/", update_product_entry_ajax, name="update_product_entry_ajax"),  
    path("product/<uuid:id>/delete-ajax/", delete_product_entry_ajax, name="delete_product_entry_ajax"),
    path("login-ajax/", login_ajax, name="login_ajax"),
    path("register-ajax/", register_ajax, name="register_ajax"),
    path("logout-ajax/", logout_ajax, name="logout_ajax"),
]