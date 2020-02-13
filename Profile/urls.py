from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User


from Profile import views

urlpatterns = [
    re_path(r'profile_lista/$', views.ProfileList.as_view()),
    re_path(r'profile_lista/nombre', views.ProfileList.as_view()),
    re_path(r'profile_lista/apePat', views.ProfileList.as_view()),
    re_path(r'profile_lista/apeMat', views.ProfileList.as_view()),
    re_path(r'profile_lista/edad', views.ProfileList.as_view()),
    re_path(r'profile_lista/genero/$', views.GeneroList.as_view()),
    re_path(r'profile_lista/ocupacion/$', views.OcupacionList.as_view()),
    re_path(r'profile_lista/ciudad/$', views.CiudadList.as_view()),
    re_path(r'profile_lista/estado/$', views.EstadoList.as_view()),
    re_path(r'profile_lista/estadoCivil/$', views.EstadoCivilList.as_view()),
    

    #Hola soy Fer
]