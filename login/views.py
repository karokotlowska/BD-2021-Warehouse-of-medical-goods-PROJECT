from django.shortcuts import render
from django.shortcuts import render,redirect
from db_handler.user import User
from . import forms

from django.http import HttpResponse


def login(request):
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            user = User()
            status = user.login(form.cleaned_data)
            id=user.get_staff_id(form.cleaned_data)
            print(id)
            if status[0] == True:
                set_session(request,status[1],id)
                #return redirect('home')
                if status[1]=='adm':
                    return render(request,'home/home.html',{'form':form,'title':'login','user_acces_admin':1})
                elif status[1]=='mag':
                    return render(request,'home/home.html',{'form':form,'title':'login','user_acces_mag':1})
                elif status[1]=='zam':
                    return render(request,'home/home.html',{'form':form,'title':'login','user_acces_zam':1})
            else:
                form = forms.loginForm()
                return render(request,'home/start_page.html',{'form':form,'title':'login','fail':status[1]})
    else:
        form = forms.loginForm()
    return render(request, 'login/login.html',{'form':form})


def set_session(request, role,id):
    request.session['user_role']=role
    request.session['user_id']=id
    

def get_session_role(request):
    try:
        return request.session['user_role']
    except KeyError:
        return None

def get_session_user_id(request):
    try:
        return request.session['user_id']
    except KeyError:
        return None

def logout(request):
    try:
        del request.session['user_role']
        del request.session['user_id']
        del request.session['redirect']
    except KeyError:
        pass
    return redirect('login')

