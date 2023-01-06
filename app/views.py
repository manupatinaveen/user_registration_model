from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse



# Create your views here.
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
            return HttpResponse('registration is successful')

    return render(request,'registration.html',d)
