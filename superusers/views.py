from django.shortcuts import render
from .models import users
from django.db.models import Q
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.views import View

# Create your views here.


#login users
class login(View):
    def get(self,request):
        return render(request, "login.html")

    
    def post(self,request):
        username  = request.POST.get('username')
        password = request.POST.get('password')
        #checking the email or phone number exist or not
        isUser  = users.objects.filter(Q(Q(email=username) or Q(phone=username)) & Q(password=password))

        if isUser.exists() and  isUser.count() ==1:
            return HttpResponseRedirect("/")      
        else:
            messages.error(request,"Invalid Cradetnials")
            return HttpResponseRedirect("/user/login")  