from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.


class UserManager(models.Manager):
    def validate(self,request):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    messages.error(request,"Please enter {}".format(key))
                    valid = False
            if len(request.POST['password'])< 8:
                valid = False
                messages.error(request,"password must have 8 characters")


            if request.POST['confirmpassword']!= request.POST['password']:
                valid = False
                messages.error(request,"password doesn't match")

            if valid == True:
                # encrypt password 
                password = request.POST['password']
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())		
                User.objects.create(name=request.POST['name'],username=request.POST['username'],password=hashed_pw )
                messages.success(request,"user created, proceed to login")
                return valid


   # def login(self,request):
      #  if request.method == "POST":
      #      valid = True
       #     username = request.POST['username']
        #    password = request.POST['password']

         #   user = User.objects.filter(username=username)
           # if len(user) > 0:
                # check password 
                # if password matches save user.id
                #else show error and redirect root
               

            #    request.session['active_id'] = user[0].id
            #    print user[0].id
            #    print user
            #    valid = True
            #    return valid

            #else:
            #    messages.error(request,"User doesn't exist ! pls register")
            #    valid = False
            #    return valid

	   



class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()




class TripManager(models.Manager):
    def validate_trip(self,request):
        if request.method == "POST":
            valid = True
            for key in request.POST:
                if request.POST[key] == "":
                    messages.error(request,"Please enter all inputs")
                    valid = False
                    return valid
                if request.POST['fromdate']> request.POST['todate']: 
                        messages.error(request,"Please select valid dates")
                        valid = False
                        return valid
                else:
                    valid = True
                    destination = request.POST['destination']
                    description = request.POST['description']
                    date_from = request.POST['fromdate']
                    date_to = request.POST['todate']
                    user= User.objects.get(id=request.session['id'])
                    trip = Trip.objects.create(destination=destination,description=description,date_from=date_from,date_to=date_to,user=user)
                    GoingonTrip.objects.create(trip=trip,user=user)
                    return valid





class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_from = models.DateTimeField() # checkthe format
    date_to = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User,related_name="trips")
    objects = TripManager()




class GoingonTrip(models.Model):
    trip = models.ForeignKey(Trip,related_name='trips')
    user = models.ForeignKey(User,related_name='users')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)





    
