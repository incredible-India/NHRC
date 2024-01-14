from django.contrib import admin
from . import views as mv
from django.urls import path
urlpatterns = [

    path('login/', mv.login.as_view(),name="login"),
   
]