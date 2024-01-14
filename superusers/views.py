from django.shortcuts import render
from .models import users
from django.db.models import Q
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.views import View
from investmentRc import middleware
from django.utils.decorators import method_decorator
from cryptography.fernet import Fernet
from django.conf import settings
# Create your views here.


#login users

class login(View):
    @method_decorator(middleware.checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            return HttpResponseRedirect("/")
        else:
            return render(request, "login.html")

    
    def post(self,request):
        username  = request.POST.get('username')
        password = request.POST.get('password')
        #checking the email or phone number exist or not
        isUser  = users.objects.filter(Q(Q(email=username) | Q(phone=username)) & Q(password=password))

        if isUser.exists() and  isUser.count() ==1:
            enckey =b'oDc1xWBsBECT3toxs8dQRJBPC85q47nRbUybtcOqJGc=' #Fernet.generate_key()#getattr(settings, 'EncKey', b'nhirc')
            fernet = Fernet(enckey)
            request.session['email'] = fernet.encrypt(username.encode('utf-8'))
            request.session['phone'] = fernet.encrypt(isUser[0].phone.encode('utf-8'))
            return HttpResponseRedirect("/user/login")
        else:
            messages.error(request,"Invalid Cradetnials")
            return HttpResponseRedirect("/user/login")  