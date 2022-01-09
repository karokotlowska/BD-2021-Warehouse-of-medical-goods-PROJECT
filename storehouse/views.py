from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages

from db_handler import zam_order
from db_handler import admin_select

from login.views import get_session_role
from .forms import CreateOrder, SelectProductToPurchase

from django.http import HttpResponse,HttpResponseRedirect, request


def create_order(request):

    form=CreateOrder
    role=get_session_role(request)
    print("rola: "+role)
    print(form.errors)
    if role=='zam':
            form=CreateOrder(request.POST)
            if form.is_valid():
                if request.method=='POST':
                    id=zam_order.zam_create_order(form.cleaned_data)
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


    