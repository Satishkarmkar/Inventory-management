"""InventoryManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory.views import *
from django.conf import settings
from django.conf.urls.static import static
# from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('admin_login',admin_login, name='admin_login'),
    path('dashboard',dashboard, name='dashboard'),
    path('add_category',add_category, name='add_category'),
    path('manage_category',manage_category, name='manage_category'),
    path('edit_category/<int:pid>',edit_category,name='edit_category'),
    path('delete_category/<int:pid>',delete_category,name='delete_category'),
    path('add_subcategory',add_subcategory, name='add_subcategory'),
    path('manage_subcategory',manage_subcategory, name='manage_subcategory'),
    path('edit_subcategory/<int:pid>',edit_subcategory,name='edit_subcategory'),
    path('delete_subcategory/<int:pid>',delete_subcategory,name='delete_subcategory'),
    path('add_brand',add_brand, name='add_brand'),
    path('manage_brand',manage_brand, name='manage_brand'),
    path('edit_brand/<int:pid>',edit_brand,name='edit_brand'),
    path('delete_brand/<int:pid>',delete_brand,name='delete_brand'),
    path('add_product',add_product, name='add_product'),
    path('manage_product',manage_product, name='manage_product'),
    path('edit_product/<int:pid>',edit_product,name='edit_product'),
    path('delete_product/<int:pid>',delete_product,name='delete_product'),
    path('load-subcategory/', load_subcategory, name='ajax_load_subcategory'),

    path('add_supplier',add_supplier, name='add_supplier'),
    path('manage_supplier',manage_supplier, name='manage_supplier'),
    path('edit_supplier/<int:suppid>',edit_supplier,name='edit_supplier'),
    path('delete_supplier/<int:suppid>',delete_supplier,name='delete_supplier'),

    path('logout',Logout, name='logout'),
    path('changepassword',changepassword, name='changepassword'),
    path('inventory',inventory, name='inventory'),
    path('search',search, name='search'),
    path('cart',cart, name='cart'),
    path('invoice_search',invoice_search, name='invoice_search'),
    path('customer_detail',customer_detail, name='customer_detail'),
    path('stock_report',stock_report, name='stock_report'),
    path('stock_reportdetails',stock_reportdetails, name='stock_reportdetails'),
    path('invoice/<int:pid>',invoice,name='invoice'),
    path('delete_cart/<int:pid>',delete_cart,name='delete_cart'),
]
