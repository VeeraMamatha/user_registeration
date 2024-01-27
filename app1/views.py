from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app1.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('registration',
            'thanksfor regestration your regestrationis Successfull'
            'mamathareddymuddam@gmail.com',
            [MUFDO.email],
            fail_silently=True)
            return HttpResponse('Registartion Is Successfull')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'registration.html',d)

def home(request):
    if request.session.get('username'):
        username=request.sessiom.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def userlogin(request):
    if request.method=='POST':
        username=request.post['un']
        password=request.post['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO) 
            requestsession['username']=username
            return HttpResponsRedirect(reverse('home'))
    return render(request,'userlogin.html') 


