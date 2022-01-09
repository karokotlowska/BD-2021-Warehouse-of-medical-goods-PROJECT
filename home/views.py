from django.shortcuts import render,redirect
from django.contrib import messages

from login.views import get_session_role


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
    if role:
        if role=='adm':
            return render(request, 'home/profile.html',{'title':'login','user_acces_admin':1})
        if role=='mag':
            return render(request, 'home/profile.html',{'title':'login','user_acces_mag':1})
        if role=='zam':
            return render(request, 'home/profile.html',{'title':'login','user_acces_zam':1})
    else:
        return HttpResponse('Brak dostępu', status=401)


    
