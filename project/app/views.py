from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1(request):
    return HttpResponse('hola amigos')
def app2(req):
    return render(req,'disco.html')
def app3(req):
    return render(req,'home.html')
def app4(req):
    return render(req,'about.html')
def app5(req):
    return render(req,'contact.html')