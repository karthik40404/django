from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def user_form(req):
    if req.method=='POST':
        form1=normal_form(req.POST)
        if form1.is_valid():
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            email=form1.cleaned_data['email']
            place=form1.cleaned_data['place']
            data=Project_user.objects.create(name=name,age=age,email=email,place=place)
            data.save()
            return redirect(user_form)
        
    form=normal_form()
    return render(req,'normalf.html',{'form':form})

def modelf(req):
    if req.method=='POST':
        form1=model_form(req.POST)
        if form1.is_valid():
            form1.save()
            return redirect(modelf)
    form=model_form()
    return render(req,'normalf.html',{'form':form})
