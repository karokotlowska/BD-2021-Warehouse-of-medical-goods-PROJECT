from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.forms import ModelForm


from db_handler import zam_order
from db_handler import admin_select
from db_handler import search_item
from db_handler import get_min_max_values
from db_handler import storehouse

from login.views import get_session_role
from .forms import SearchOrder,SelectProductToReceive,SelectProductToPurchase,SearchStorehouse,SelectProductToPurchase2

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
    if id=='error':
        messages.success(request, 'Takie zamówienie nie istnieje.')
        form=SearchOrder
        return render(request, 'storehouse_action_handler/search_by_id.html', {'form':form,'form_title':['przyjmij','zamówienie']})
    else:
        select2=admin_select.order_details(id)
        #select=admin_select.admin_order_view_select(int(id))

        form=SelectProductToReceive(request.GET)
        if form.is_valid():
                if request.method=='POST':
                        print('drugipostDZINWY')
                        #zam_order.zam_insert_product(form.cleaned_data,id)
                return render(request,'storehouse_action_handler/show_receipt.html',{'form':form,'select2':select2, 'numer_kolejny_zamowienia':id})
    

def add_product(request):
    numer_kolejny_zamowienia=request.GET.get('id')
    user_id=request.session['user_id']
    select=admin_select.admin_order_view_select(int(numer_kolejny_zamowienia))
    form=SelectProductToPurchase(request.POST)
    select2=admin_select.order_details(numer_kolejny_zamowienia)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipost')
                    print("-----------------------")
                    error=zam_order.zam_receipt_product(form.cleaned_data,numer_kolejny_zamowienia,user_id)
                    select=admin_select.admin_order_view_select(int(numer_kolejny_zamowienia))

                    messages.success(request, 'Przyjęto produkt.')
       

            return render(request,'storehouse_action_handler/add_product_to_storehouse.html',{'form':form,'form_title':['PRZYMIJ PRODUKTY NA MAGAZYN',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':numer_kolejny_zamowienia})



def removal(request):
    
    products=admin_select.productListForSearch() 
    role=get_session_role(request)

    print("rola: "+role)
    form=SearchStorehouse
    data = search_item.storehouse_view_all()
    if role=='mag':
            form=SearchStorehouse(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    return search_order_view_remove(request, form.cleaned_data)
                return render(request, 'storehouse_action_handler/search_by_id_removal.html', {'form':form,'data':data,'products':products,'form_title':['wydaj','produkty'],'numer_kolejny_zamowienia':id})     
    else:
        return HttpResponse('Brak dostępu', status=401)


def search_order_view_remove(request, form_data):
        user_id=request.session['user_id']
     
        select2=admin_select.storehouse_view(form_data['magazyn'])
     

        #form=SelectProductToPurchase2(form_data['magazyn'],request.GET)
        if True:
            if request.method=='POST':
                    print('drugipostDZINWY')
                   
                    #zam_order.zam_insert_product(form.cleaned_data,id)
        return render(request,'storehouse_action_handler/removal_show_all.html',{'select2':select2,'form_title':['wydaj','produkty'],'numer_kolejny_zamowienia':form_data['magazyn']})

def remove_product(request):
    id_magazynu=request.GET.get('id')
    select2=admin_select.storehouse_view(id_magazynu)
    id_prac=request.session['user_id']

    #form=SelectProductToPurchase()
    list_of_choices=admin_select.productListFromMagazyn(id_magazynu)
    form=SelectProductToPurchase2(request.POST,my_choices=list_of_choices)
    
    if form.is_valid():
        if request.method=='POST':

                error=storehouse.removal(id_magazynu,form.cleaned_data,id_prac)
                select2=admin_select.storehouse_view(id_magazynu)
                if error=='error':
                    messages.success(request, 'Nie można wydać produktów')

                else:
                    messages.success(request, 'Wydano produkt.')

    return render(request,'storehouse_action_handler/remove_product.html',{'form':form,'form_title':['WYDAJ PRODUKTY Z MAGAZYNU',""],'select2':select2, 'numer_kolejny_zamowienia':id_magazynu})



def render_search_orders_site(request,data):
    products=admin_select.productList()     #wszytskie produkty
    print(products)
    filters_min_max_values = get_min_max_values.get_min_max_values()
    return render(request,'storehouse_action_handler/search_storehouse.html',{'data':data,'products':products,'filters_limits':filters_min_max_values})


def searchoperations(request):
    data = search_item.filter_storehouse(request.GET)  #zwrocone zamowienia ktore spelniaja warunki
    #request.session['mag'] = request.build_absolute_uri()
    return render_search_orders_site(request,data)
