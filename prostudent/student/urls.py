from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('edit/<a>',views.edt_std),
    path('delete/<a>',views.dele),
]
