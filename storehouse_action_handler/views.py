from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages

from db_handler import zam_order
from db_handler import admin_select
from db_handler import search_item
from db_handler import get_min_max_values
from db_handler import storehouse

from login.views import get_session_role
from .forms import SearchOrder,SelectProductToReceive,SelectProductToPurchase,SelectProductToPurchase2

from django.http import HttpResponse,HttpResponseRedirect, request




def receipt(request):
    form=SearchOrder
    role=get_session_role(request)
    print("rola: "+role)
    print(form.errors)
    if role=='mag':
            form=SearchOrder(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    return search_order_view(request, form.cleaned_data)
                return render(request, 'storehouse_action_handler/search_by_id.html', {'form':form,'form_title':['przyjmij','zamówienie']})     
    else:
        return HttpResponse('Brak dostępu', status=401)



def search_order_view(request, form_data):
    id=zam_order.get_order_id(form_data['id_zamowienia'])
    select2=admin_select.edit_order_details(form_data['id_zamowienia'])
    form=SelectProductToReceive(request.GET)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipostDZINWY')
                    #zam_order.zam_insert_product(form.cleaned_data,id)
            return render(request,'storehouse_action_handler/show_receipt.html',{'form':form,'select2':select2, 'numer_kolejny_zamowienia':id})

def add_product(request):
    id=request.GET.get('id')
    user_id=request.session['user_id']
    select=admin_select.admin_order_view_select(int(id))
    form=SelectProductToPurchase(request.POST)
    select2=admin_select.order_details(id)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipost')
                    error=zam_order.zam_receipt_product(form.cleaned_data,id,user_id)
                    if error =='error':
                        select2=admin_select.order_details(id)
                        messages.error(request, 'Brak zamówienia na ten produkt.')

                    else:
                        messages.success(request, 'Przyjęto produkt.')

            return render(request,'storehouse_action_handler/add_product_to_storehouse.html',{'form':form,'form_title':['PRZYMIJ PRODUKTY NA MAGAZYN',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})



def removal(request):
    
    role=get_session_role(request)
    print("rola: "+role)
    form=SelectProductToPurchase
    if role=='mag':
            form=SelectProductToPurchase(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    return search_order_view_remove(request, form.cleaned_data)
                return render(request, 'storehouse_action_handler/search_by_id_removal.html', {'form':form,'form_title':['wydaj','produkty']})     
    else:
        return HttpResponse('Brak dostępu', status=401)


def search_order_view_remove(request, form_data):
        user_id=request.session['user_id']
        id=request.GET.get('id')
        select2=admin_select.storehouse_view(form_data['magazyn'])
        print(select2)
        form=SelectProductToPurchase(request.GET)
        if form.is_valid():
            if request.method=='POST':
                    print('drugipostDZINWY')
                    error=storehouse.removal(form_data['magazyn'],form_data['ilosc'],form_data['produkt'],user_id)
                    select2=admin_select.storehouse_view(form_data['magazyn'])
                    if error=='error':
                        messages.success(request, 'Błędna ilość produktów do wydania, bądź taki produkt nie jest na magazynie.')

                    else:
                        messages.success(request, 'Wydano produkt.')

                    #zam_order.zam_insert_product(form.cleaned_data,id)
            return render(request,'storehouse_action_handler/removal_show_all.html',{'form':form,'select2':select2,'form_title':['wydaj','produkty']})


def render_search_orders_site(request,data):
    products=admin_select.productListForSearch()     #wszytskie produkty
    filters_min_max_values = get_min_max_values.get_min_max_values()
    return render(request,'storehouse_action_handler/search_storehouse.html',{'data':data,'products':products,'filters_limits':filters_min_max_values})


def searchoperations(request):
    data = search_item.filter_storehouse(request.GET)  #zwrocone zamowienia ktore spelniaja warunki
    request.session['mag'] = request.build_absolute_uri()
    return render_search_orders_site(request,data)
