#checking the user verifications...
#if user is logged in we will show direct profile page and if not we will send response for creating account or login page and
from superusers.models import users 
from django.db.models import Q
from django.conf import settings
from cryptography.fernet import Fernet


class checkingUserAuthentication:
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        if 'email' in request.session:
            if 'phone' in request.session:
                enckey =  b'oDc1xWBsBECT3toxs8dQRJBPC85q47nRbUybtcOqJGc='
                print("<----------------------------")
                fernet = Fernet(enckey)
                print("<----------------------------",request.session['email'],type(request.session['email']))
                email=fernet.decrypt(request.session['email']).decode()
                phone=fernet.decrypt(request.session['phone']).decode()
                print(email.phone,"<----------------------------")
                isExist = users.objects.filter(Q(email=email)& Q(phone=phone))
                if len(isExist) == 1:
                    request.phone = phone
                    request.email = email
                    request.isauth = True
                else:
                    request.isauth = False
                    
            else:
                    request.isauth = False
        else:
                request.isauth = False

        
        response = self.get_response(request)

        return response

                