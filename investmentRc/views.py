from django.shortcuts import render,HttpResponseRedirect
from django.utils.decorators import method_decorator
from investmentRc import middleware
from django.views import View
class index(View):
    @method_decorator(middleware.checkingUserAuthentication)
    def get(self,request):
        if request.isauth:
            return render(request,'index.html')
        else:
            return HttpResponseRedirect("user/login")