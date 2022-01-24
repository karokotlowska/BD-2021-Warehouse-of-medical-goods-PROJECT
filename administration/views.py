from email import message
from django.shortcuts import render,redirect


from login.views import get_session_role

from . import forms
from django.contrib import messages
from db_handler import admin_insert
from db_handler import admin_select
from db_handler import admin_update
from db_handler import admin_delete

from administration.forms import InsertPracownik_stanowisko
from administration.forms import InsertPracownik, InsertKontrahent

from administration.forms import UpdateWeryfikacja, InsertOperacja
from administration.forms import UpdatePracownik, UpdateLokalizacja
from administration.forms import UpdatePracownik_stanowisko

from administration.forms import DeletePracownik_stanowisko, DeleteProduct
from administration.forms import DeletePracownik, InsertProdukt, InsertKategoria, InsertLokalizacja

from django.http import HttpResponse



def operations(request):
    role=get_session_role(request)
    if role=='adm':
        return render(request, 'administration/admin_panel.html')
    else:
        return HttpResponse('Brak dostępu', status=401)


def manage(request):
        method = request.GET.get('method')
        if method == 'insert':
            resource = request.GET.get('resource')
            return insert_form(request,resource)
        elif method=='select':
            resource = request.GET.get('resource')
            return select_form(request, resource)
        elif method=='update':
            resource = request.GET.get('resource')
            return update_form(request, resource)
        elif method=='delete':
            resource = request.GET.get('resource')
            return delete_form(request, resource)

            

def insert_form(request,resource):
    if resource == 'pracownik':
        form = InsertPracownik
        if request.method == 'POST':
            form = InsertPracownik(request.POST)
            if form.is_valid():
                er=admin_insert.insert_pracownik(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd dodawania.')
                else:
                    messages.success(request, 'Dodano.')
                #return redirect('forms')
    elif resource == 'pracownik_stanowisko':
        form = InsertPracownik_stanowisko
        if request.method == 'POST':
            form = InsertPracownik_stanowisko(request.POST)
            if form.is_valid():
                er=admin_insert.insert_pracownik_stanowisko(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Sprawdź czy id_stanowisko ma co najwyżej trzy litery lub czy takie stanowisko już istnieje.')
                else:
                    messages.success(request, 'Dodano stanowisko.')

    elif resource == 'produkt':
        form = InsertProdukt
        if request.method == 'POST':
            form = InsertProdukt(request.POST)
            if form.is_valid():
                er=admin_insert.insert_produkt(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błędna kategoria produktu.')
                else:
                    messages.success(request, 'Dodano produkt.')
    elif resource =='lokalizacja_magazynu':
        form = InsertLokalizacja
        if request.method == 'POST':
            form = InsertLokalizacja(request.POST)
            if form.is_valid():
                er=admin_insert.insert_lokalizacja(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd dodawania.')
                else:
                    messages.success(request, 'Dodano lokalizację.')

    elif resource =='kategoria':
        form = InsertKategoria
        if request.method == 'POST':
            form = InsertKategoria(request.POST)
            if form.is_valid():
                er=admin_insert.insert_kategoria(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd dodawania - najprawdopodobniej taka kategoria już istnieje.')
                else:
                    messages.success(request, 'Dodano kategorię.')
    elif resource =='kontrahent':
        form = InsertKontrahent
        if request.method == 'POST':
            form = InsertKontrahent(request.POST)
            if form.is_valid():
                er=admin_insert.insert_kontrahent(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd dodawania.')
                else:
                    messages.success(request, 'Dodano kontrahenta.')
    elif resource =='rodzaj_operacji':
        form = InsertOperacja
        if request.method == 'POST':
            form = InsertOperacja(request.POST)
            if form.is_valid():
                er=admin_insert.insert_rodzaj_operacji(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd dodawania.')
                else:
                    messages.success(request, 'Dodano rodzaj operacji.')
    else:
        return redirect('home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['insert',resource]})


def delete_form(request, resource):
    if resource=='pracownik_stanowisko':
        form = DeletePracownik_stanowisko
        if request.method == 'POST':
            form = DeletePracownik_stanowisko(request.POST)
            if form.is_valid():
                er=admin_delete.delete_pracownik_stanowisko(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd usuwania.')
                else:
                    messages.success(request, 'usunięto.')
    elif resource=='pracownik':
        form = DeletePracownik
        if request.method == 'POST':
            form = DeletePracownik(request.POST)
            if form.is_valid():
                er=admin_delete.delete_pracownik(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd usuwania.')
                else:
                    messages.success(request, 'usunięto.')
    elif resource=='produkt':
        form = DeleteProduct
        if request.method == 'POST':
            form = DeleteProduct(request.POST)
            if form.is_valid():
                er=admin_delete.delete_produkt(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd usuwania.')
                else:
                    messages.success(request, 'usunięto.')
    else:
        return redirect('home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['delete',resource]})
        

def select_form(request, resource):
    if resource == 'magazyn':
        select=admin_select.admin_magazyn_stan_view(resource)
        return render(request,'administration/show_forms.html',{'select':select})
    if resource == 'pracownik':
        select=admin_select.admin_pracownik_view(resource)
        return render(request,'administration/show_forms.html',{'select':select})
    if resource == 'produkty':
        select=admin_select.admin_produkty_view(resource)
        return render(request,'administration/show_forms.html',{'select':select})
    
    if resource =='pokaz_zamowienia':
        select=admin_select.admin_zamowienie_view(resource)
        print("11")
        return render(request,'administration/show_forms.html',{'select':select})
     
    else:
        select=admin_select.admin_dict_select(resource)
        return render(request,'administration/show_forms.html',{'select':select})

def update_form(request, resource):
    if resource=='weryfikacja':
        form = UpdateWeryfikacja
        if request.method == 'POST':
            form = UpdateWeryfikacja(request.POST)
            if form.is_valid():
                er=admin_update.update_weryfikacja(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd wprowadzania zmian.')
                else:
                    messages.success(request, 'Zmieniono.')
    elif resource=='pracownik':
        form = UpdatePracownik
        if request.method == 'POST':
            form = UpdatePracownik(request.POST)
            if form.is_valid():
                er=admin_update.update_pracownik(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd wprowadzania zmian.')
                else:
                    messages.success(request, 'Zmieniono.')
    elif resource=='pracownik_stanowisko':
        form = UpdatePracownik_stanowisko
        if request.method == 'POST':
            form = UpdatePracownik_stanowisko(request.POST)
            if form.is_valid():
                er=admin_update.update_pracownik_stanowisko(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd wprowadzania zmian.')
                else:
                    messages.success(request, 'Zmieniono.')
    elif resource=='lokalizacja_magazynu':
        form = UpdateLokalizacja
        if request.method == 'POST':
            form = UpdateLokalizacja(request.POST)
            if form.is_valid():
                er=admin_update.update_lokalizacja(form.cleaned_data)
                if er=='error':
                    messages.success(request, 'Błąd wprowadzania zmian.')
                else:
                    messages.success(request, 'Zmieniono.')
    else:
        return redirect('home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['update',resource]})
