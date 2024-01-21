from django.contrib import admin
from .models import users,UserRecord
# Register your models here.
@admin.register(users)
class usersADMIN(admin.ModelAdmin):
    list_display = ['id','name','email','phone','password','address','account','userimg','gender']
@admin.register(UserRecord)
class UserRecordADMIN(admin.ModelAdmin):
    list_display = ['id','userid','InvetsMentType','InvetsMentCategory','Ammount']