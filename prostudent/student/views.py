from django.shortcuts import render , redirect

# Create your views here.

std=[]

def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        classes=req.POST['classes']
        std.append({'roll_no':roll,'name':name,'age':age,'classes':classes})
        # print(std)
        return redirect(home)
    else:
        return render(req,'home.html',{'students':std})