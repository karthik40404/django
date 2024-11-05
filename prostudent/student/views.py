from django.shortcuts import render , redirect

# Create your views here.

std=[{'roll_no':'1','name':'kar','age':'4','classes':'2'},{'roll_no':'2','name':'wer','age':'66','classes':'4'}]

def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        classes=req.POST['classes']
        std.append({'roll_no':roll,'name':name,'age':age,'classes':classes})
        return redirect(home)
    else:
        return render(req,'home.html',{'students':std})
    
def edt_std(req,a):
    data=''
    for i in std:
        if i ['roll_no']==a:
            data=i
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        classes=req.POST['classes']
        data['roll_no']=roll
        data['name']=name
        data['age']=age
        data['classes']=classes
        return redirect(home)
    else:
        return render(req,'edit.html',{'data':data})
    
def dele(req,a):
    for i in std:
        if i ['roll_no']==a:
            std.remove(i)
    return redirect (home)
