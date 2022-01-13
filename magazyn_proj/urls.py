"""magazyn_med_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from home import views as home_views
from login import views as login_views 
from administration import views as administration_views
from storehouse import views as storehouse_views
from storehouse_action_handler import views as storehouse_action_handler_views



urlpatterns = [
    path('', home_views.start_page, name = "start_page"),
    path('home/', home_views.home,name = "home"),
    path('profile/',home_views.profile,name = "profile"),


    path('login/', login_views.login,name = "login"),
    path('logout/', login_views.logout,name = "logout"),


    path('admin_panel/', administration_views.operations,name = "operations"),
    path('manage/', administration_views.manage, name='manage'),

    
    path('createorder/', storehouse_views.create_order, name='createorder'),
    path('createorder/order_view/', storehouse_views.order_view, name='order_view'),
    path('add_product/', storehouse_views.add_product, name='add_product'),
    path('del_product/', storehouse_views.del_product, name='del_product'),
    path('change_order_status/', storehouse_views.change_order_status, name='change_order_status'),
    path('editorder/', storehouse_views.edit_order, name='editorder'),
    path('searchorders/', storehouse_views.search_orders, name='searchorders'),


    path('receipt/', storehouse_action_handler_views.receipt, name='receipt'),
    path('removal/', storehouse_action_handler_views.removal, name='removal'),
    path('searchoperations/', storehouse_action_handler_views.searchoperations, name='searchoperations'),

    path('add_product_to_storehoue/', storehouse_action_handler_views.add_product, name='add_product_to_storehoue'),




]
