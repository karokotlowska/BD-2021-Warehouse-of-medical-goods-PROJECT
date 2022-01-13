from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages

from db_handler import zam_order
from db_handler import admin_select
from db_handler import search_item
from db_handler import get_min_max_values

from login.views import get_session_role
from .forms import CreateOrder, SelectProductToPurchase, EditOrder,ProductToDelete,OrderStatus

from django.http import HttpResponse,HttpResponseRedirect, request


def create_order(request):
    form=CreateOrder
    role=get_session_role(request)
    user_id=request.session['user_id']
    print("rola: "+role)
    print(form.errors)
    if role=='zam':
            form=CreateOrder(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    id=zam_order.zam_create_order(form.cleaned_data,user_id)
                    #return redirect(request,'home')
                    print('pierwszypost')
                    messages.success(request, 'Dodano zamówienie.')

                    return order_view(request, id)
                return render(request, 'storehouse/create_order.html', {'form':form,'form_title':['dodaj','zamówienie']})     
    else:
        return HttpResponse('Brak dostępu', status=401)


def order_view(request, id):
    #select=zam_order.storehouse_order_select(resource)
    select=admin_select.admin_order_view_select(id)
    select2=admin_select.order_details(id)
    form=SelectProductToPurchase(request.GET)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipostDZINWY')
                    #zam_order.zam_insert_product(form.cleaned_data,id)
            return render(request,'storehouse/show_order.html',{'form':form,'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})


def add_product(request):
    id=request.GET.get('id')
    print(id)
    select=admin_select.admin_order_view_select(int(id))
    form=SelectProductToPurchase(request.POST)
    select2=admin_select.order_details(id)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipost')
                    zam_order.zam_insert_product(form.cleaned_data,id)
                    select2=admin_select.order_details(id)
                    messages.success(request, 'Dodano produkt.')

            return render(request,'storehouse/add_product.html',{'form':form,'form_title':['DODAJ PRODUKTY DO ZAMÓWIENIA',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})


def del_product(request):
    id=request.GET.get('id')
    select=admin_select.admin_order_view_select(int(id))
    form=ProductToDelete(request.POST)
    select2=admin_select.order_details(id)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipost')
                    zam_order.zam_del_product(form.cleaned_data,id)
                    select2=admin_select.order_details(id)
                    messages.success(request, 'Usunięto produkt.')

            return render(request,'storehouse/del_product.html',{'form':form,'form_title':['WYBIERZ PRODUKT DO USUNIĘCIA',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})


def change_order_status(request):
    id=request.GET.get('id')
    select=admin_select.admin_order_view_select(int(id))
    form=OrderStatus(request.POST)
    select2=admin_select.order_details(id)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipost')
                    zam_order.zam_chenge_status(form.cleaned_data,id)
                    select2=admin_select.order_details(id)
                    messages.success(request, 'Zmieniono status.')

            return render(request,'storehouse/change_order_status.html',{'form':form,'form_title':['ZMIEŃ STATUS',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})




def edit_order(request):
    form=EditOrder
    role=get_session_role(request)
    print("rola: "+role)
    print(form.errors)
    if role=='zam':
            form=EditOrder(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    return edit_order_view(request, form.cleaned_data)
                return render(request, 'storehouse/editorder.html', {'form':form,'form_title':['edytuj','zamówienie']})     
    else:
        return HttpResponse('Brak dostępu', status=401)
 
def edit_order_view(request, form_data):
    id=zam_order.get_order_id(form_data['id_zamowienia'])
    #select=zam_order.storehouse_order_select(resource)
    select2=admin_select.edit_order_details(form_data['id_zamowienia'])
    form=SelectProductToPurchase(request.GET)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipostDZINWY')
                    #zam_order.zam_insert_product(form.cleaned_data,id)
            return render(request,'storehouse/show_edit_order.html',{'form':form,'select2':select2, 'numer_kolejny_zamowienia':id})


def render_search_site(request,data):
    products=admin_select.productListForSearch()     #wszytskie produkty
    filters_min_max_values = get_min_max_values.get_min_max_values()
    return render(request,'storehouse/search_orders.html',{'data':data,'products':products,'filters_limits':filters_min_max_values})


def search_orders(request):
    data = search_item.filter(request.GET)  #zwrocone zamowienia ktore spelniaja warunki
    request.session['zam'] = request.build_absolute_uri()
    return render_search_site(request,data)

'''def search_orders(request):
    data = search_item.filter(request.GET)  #zwrocone zamowienia ktore spelniaja warunki
    products=admin_select.productListForSearch()     #wszytskie produkty
    filters_min_max_values = get_min_max_values.get_min_max_values()
    return render(request,'storehouse/search_orders.html',{'data':data,'products':products,'filters_limits':filters_min_max_values})
'''

'''def create_order(request):


    role=get_session_role(request)
    print("rola: "+role)

    if role=='zam':
            form=CreateOrder(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    id=zam_order.zam_create_order(form.cleaned_data)
                    #return redirect(request,'home')
                    print('pierwszypost')
                    #return HttpResponseRedirect('order_view',form.cleaned_data['id_zamowienia'], id)
                    #return render(request,'storehouse/show_order.html',{'form':form,'id': id})
                return render(request, 'storehouse/create_order.html', {'form':form,'form_title':['dodaj','zamówienie']})     
    else:
        return HttpResponse('Brak dostępu', status=401)


def order_view(request, resource, id):
    #select=zam_order.storehouse_order_select(resource)
    select=admin_select.admin_order_view_select(resource,id)
    select2=admin_select.order_details(id)
    form=SelectProductToPurchase(request.GET)
    if form.is_valid():
            if request.method=='POST':
                    print('drugipost')
                    #zam_order.zam_insert_product(form.cleaned_data,id)
            return render(request,'storehouse/show_order.html',{'form':form,'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})
'''

'''def create_order(request):
    #form=CreateOrder(request.POST)
    role=get_session_role(request)
    print("rola: "+role)
    #print(form.errors)
    if role=='zam':
        #if form.is_valid():
        #return create_order_form_handler(request)
            #zam_order.zam_create_order(form.cleaned_data)
        return render(request, 'storehouse/create_order.html', {'form':form,'form_title':['select','produkt']})     
    else:
        return HttpResponse('Brak dostępu', status=401)

def create_order_form_handler(request):
    form=CreateOrder(request.POST)
    if form.is_valid():
        print("lalalalalla")
        zam_order.zam_create_order(form.cleaned_data)
        return render(request, 'storehouse/create_order.html', {'form':form,'form_title':['select','produkt']}) 
'''
def storehouse_view_order(request):
    form=SelectProductToPurchase(request.GET)
    role=get_session_role(request)
    print("rola: "+role)
    print(form.errors)
    if role=='zam':
        if form.is_valid():
            if request.method=='POST':
                return render(request, 'storehouse/order.html', {'form':form,'form_title':['select','produkt']})     
    else:
        return HttpResponse('Brak dostępu', status=401)
    return render(request, 'storehouse/order.html', {'form':form,'form_title':['select','produkt']})     


    