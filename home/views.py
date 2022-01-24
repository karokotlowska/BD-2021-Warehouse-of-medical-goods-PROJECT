from django.shortcuts import render,redirect
from django.contrib import messages

from login.views import get_session_role

from db_handler import admin_select
from django.http import HttpResponse

#logged user home
def home(request):
    return render(request, 'home/home.html')

#logout user home
def start_page(request):
    return render(request,'home/start_page.html',{'title':'start page','option':'home'})

def profile(request):
    role=get_session_role(request)
    print("rola: "+role)
    id=request.session['user_id']
    print(id)
    if role:
        if role=='adm':
            select=admin_select.admin_profile_select("Dane:",id)
            return render(request,'home/profile.html',{'select':select,'title':'login','user_acces_admin':1})
            #return render(request, 'home/profile.html',{'title':'login','user_acces_admin':1})
        if role=='mag':
            select=admin_select.admin_profile_select("Dane:",id)
            return render(request,'home/profile.html',{'select':select,'title':'login','user_acces_mag':1})
            #return render(request, 'home/profile.html',{'title':'login','user_acces_mag':1})
        if role=='zam':
            select=admin_select.admin_profile_select("Dane:",id)
            return render(request,'home/profile.html',{'select':select,'title':'login','user_acces_zam':1})
            #return render(request, 'home/profile.html',{'title':'login','user_acces_zam':1})
        if role=='error':
            return render(request, 'home/home.html')

    else:
        return HttpResponse('Brak dostępu', status=401)
