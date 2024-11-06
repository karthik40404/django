from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('edit/<id>',views.edt_std),
    path('delete/<id>',views.dele),
]
