from django.db import models
import datetime 
# Create your models here.
class users(models.Model):
    GENDER_CHOICES	=	(('male',	'Male'),('female',	'Female'),('transgender',	'Transgender'),)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=250)
    address = models.TextField()
    account = models.DateTimeField(default=datetime.datetime.now(), blank=True,null=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='male')
    userimg = models.ImageField(upload_to='userimg/' ,null=True)


#User Records including individual and Common records
class UserRecord(models.Model):
    userid = models.ForeignKey(users,on_delete=models.CASCADE)
    Investment_type	=	(('individual',	'Individual'),('common',	'Common'))
    Investment_category	=	(('Equity',	'Equity'),('Crypto',	'Crypto'),('Mutual Fund',	'Mutual Fund'),("F&O","Future and Options"),('Other',	'Other'))
    InvetsMentType = models.CharField(max_length=20,choices= Investment_type,default='individual')
    InvetsMentCategory = models.CharField(max_length=20,choices= Investment_category,default='Equity')
    Ammount =  models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

