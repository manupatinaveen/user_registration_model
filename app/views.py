from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail



# Create your views here.
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')
def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            PW=UD.cleaned_data['password']
            USO=UD.save(commit=False)
            USO.set_password(PW) 
            USO.save() 

            PFO=PD.save(commit=False)
            PFO.user=USO
            PFO.save()

            send_mail('registration',
            'successfull',
            'manupatinaveen2000@gmail.com',
            [USO.email],
            fail_silently=False)

            return HttpResponse('registration is successful')

    return render(request,'registration.html',d)
