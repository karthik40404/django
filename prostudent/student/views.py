from django.shortcuts import render , redirect
from .models import *

# Create your views here.

# std=[{'roll_no':'1','name':'kar','age':'4','classes':'2'},{'roll_no':'2','name':'wer','age':'66','classes':'4'}]

def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        classes=req.POST['classes']
        # std.append({'roll_no':roll,'name':name,'age':age,'classes':classes})
        data=Student.objects.create(roll_no=roll,name=name,age=age,classes=classes)
        data.save()
        return redirect(home)
    else:
        data=Student.objects.all()
        return render(req,'home.html',{'students':data})
    
def edt_std(req,id):
    # data=''
    # for i in data:
    #     if i ['roll_no']==a:
    #         data=i
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        classes=req.POST['classes']
        # data['roll_no']=roll
        # data['name']=name
        # data['age']=age
        # data['classes']=classes
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age,classes=classes)
        return redirect(home)
    else:
        data=Student.objects.get(pk=id)
        return render(req,'edit.html',{'data':data})
    
def dele(req,id):
    # for i in std:
    #     if i ['roll_no']==a:
    #         std.remove(i)
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect (home)
