from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages

from db_handler import zam_order
from db_handler import admin_select
from db_handler import search_item
from db_handler import get_min_max_values

from login.views import get_session_role
from .forms import CreateOrder, SelectProductToPurchase,Payment, EditOrder,ProductToDelete,OrderStatus

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
                    if id=='error':
                        messages.success(request, 'Takie zamowienie już istnieje.')
                    else:
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
                    print('ok')
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
                    er=zam_order.zam_insert_product(form.cleaned_data,id)
                    if er=='error':
                        messages.success(request, 'Już dodano ten produkt.')
                    else:
                        select2=admin_select.order_details(id)
                        select=admin_select.admin_order_view_select(int(id))

                        messages.success(request, 'Dodano produkt.')

            return render(request,'storehouse/add_product.html',{'form':form,'form_title':['DODAJ PRODUKTY DO ZAMÓWIENIA',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})



def del_product(request):
    id=request.GET.get('id')
    select=admin_select.admin_order_view_select(int(id))
    form=ProductToDelete(request.POST)
    select2=admin_select.order_details(id)
    if form.is_valid():
            if request.method=='POST':
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
                    zam_order.zam_chenge_status(form.cleaned_data,id)
                    select2=admin_select.order_details(id)
                    messages.success(request, 'Zmieniono status.')

            return render(request,'storehouse/change_order_status.html',{'form':form,'form_title':['ZMIEŃ STATUS',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})


def add_payment(request):
    id=request.GET.get('id')
    select=admin_select.admin_order_view_select(int(id))
    form=Payment(request.POST)
    select2=admin_select.order_details(id)
    if form.is_valid():
            if request.method=='POST':
                    zam_order.zam_add_payment(form.cleaned_data,id)
                    select2=admin_select.order_details(id)
                    messages.success(request, 'Dodano płatność.')

            return render(request,'storehouse/add_payment.html',{'form':form,'form_title':['Płatność',""],'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})


def edit_order(request):
    form=EditOrder
    role=get_session_role(request)
    print("rola: "+role)
    if role=='zam':
            form=EditOrder(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    return edit_order_view(request, form.cleaned_data)
                return render(request, 'storehouse/editorder.html', {'form':form,'form_title':['edytuj','zamówienie']})     
    else:
        return HttpResponse('Brak dostępu', status=401)
 
def edit_order_view(request, form_data):
    id_zamowienia=form_data['id_zamowienia']
    id_zamowienia=id_zamowienia.upper()
    id=zam_order.get_order_id(id_zamowienia)
    select=admin_select.admin_order_view_select(int(id))
    select2=admin_select.order_details(id)

    if id!='error':
        #select=zam_order.storehouse_order_select(resource)
        #select2=admin_select.edit_order_details(id_zamowienia)
        form=SelectProductToPurchase(request.GET)
        if form.is_valid():
                if request.method=='POST':
                        print('drugipostDZINWY')
                        #zam_order.zam_insert_product(form.cleaned_data,id)
                return render(request,'storehouse/show_edit_order.html',{'form':form,'select':select,'select2':select2, 'numer_kolejny_zamowienia':id})
    else:
        messages.success(request, 'Takie zamówienie nie istnieje.')
        return redirect('editorder')


def render_search_site(request,data):
    products=admin_select.productListForSearch()     #wszytskie produkty
    print(products)
    print("kkk")
    filters_min_max_values = get_min_max_values.get_min_max_values()
    return render(request,'storehouse/search_orders.html',{'data':data,'products':products,'filters_limits':filters_min_max_values})


def search_orders(request):
    data = search_item.filter(request.GET)  #zwrocone zamowienia ktore spelniaja warunki
    request.session['zam'] = request.build_absolute_uri()
    return render_search_site(request,data)


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


    