from django.shortcuts import render,redirect


from login.views import get_session_role

from . import forms
from django.contrib import messages
from db_handler import admin_insert
from db_handler import admin_select
from db_handler import admin_update
from db_handler import admin_delete

from administration.forms import InsertPracownik_stanowisko
from administration.forms import InsertPracownik

from administration.forms import UpdateWeryfikacja
from administration.forms import UpdatePracownik
from administration.forms import UpdatePracownik_stanowisko

from administration.forms import DeletePracownik_stanowisko
from administration.forms import DeletePracownik

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
                admin_insert.insert_pracownik(form.cleaned_data)
                return redirect('forms')
    elif resource == 'pracownik_stanowisko':
        form = InsertPracownik_stanowisko
        if request.method == 'POST':
            form = InsertPracownik_stanowisko(request.POST)
            if form.is_valid():
                admin_insert.insert_pracownik_stanowisko(form.cleaned_data)
                return redirect('forms')
    
    else:
        return redirect('home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['insert',resource]})


def delete_form(request, resource):
    if resource=='pracownik_stanowisko':
        form = DeletePracownik_stanowisko
        if request.method == 'POST':
            form = DeletePracownik_stanowisko(request.POST)
            if form.is_valid():
                admin_delete.delete_pracownik_stanowisko(form.cleaned_data)
                return redirect('admin_panel')
    elif resource=='pracownik':
        form = DeletePracownik
        if request.method == 'POST':
            form = DeletePracownik(request.POST)
            if form.is_valid():
                admin_delete.delete_pracownik(form.cleaned_data)
                return redirect('admin_panel')
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
                admin_update.update_weryfikacja(form.cleaned_data)
                return redirect('admin_panel')
    elif resource=='pracownik':
        form = UpdatePracownik
        if request.method == 'POST':
            form = UpdatePracownik(request.POST)
            if form.is_valid():
                admin_update.update_pracownik(form.cleaned_data)
                return redirect('admin_panel')
    elif resource=='pracownik_stanowisko':
        form = UpdatePracownik_stanowisko
        if request.method == 'POST':
            form = UpdatePracownik_stanowisko(request.POST)
            if form.is_valid():
                admin_update.update_pracownik_stanowisko(form.cleaned_data)
                return redirect('admin_panel')
    else:
        return redirect('home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['update',resource]})
