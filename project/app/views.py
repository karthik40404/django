from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def app1(request):
    return HttpResponse('hola amigos')
def app2(req):
    return render(req,'disco.html')

l=[]
def app3(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        l.append({'name':name,'age':age})
        print(l)
        return redirect(app3)
    else:
        return render(req,'home.html')
    
def app4(req):
    return render(req,'about.html')
def app5(req):
    return render(req,'contact.html')


l=[{'name':'kar','age':'33'},{'name':'thi','age':'35'}]
def display(req):
    return render(req,'display.html',{'data':l})


def add_details(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        l.append({'name':name,'age':age})
        print(l)
        return redirect(display)
    else:
        return render(req,'add_details.html')