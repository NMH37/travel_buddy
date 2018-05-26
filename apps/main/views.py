from django.shortcuts import render,redirect,HttpResponse
from models import User,Trip,GoingonTrip
import bcrypt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages


def index(request):
    return render(request,'main/index.html')



def register(request):
    User.objects.validate(request)
    return redirect('/')


def dashboard(request):
    user= User.objects.get(id=request.session['id'])
   
    context = { 
           'user' : User.objects.get(id = request.session['id']),
           'all_users':Trip.objects.exclude(user=user)
    }
    return render(request,'main/dashboard.html',context)

def add_trip(request):
    return render(request,'main/add_trip.html')

def addtrip(request):
    if request.method == "POST":
        valid = Trip.objects.validate_trip(request)
        if valid: # print trip added
            print "trip added"
            return redirect('/dashboard') # redirect to dash board
        else:
            return redirect('/add_trip')


#def login(request):
    #User.objects.login(request)   
    #return redirect('/dashboard')

def login(request):

	username = request.POST['username']
	password = request.POST['password']

	user = User.objects.filter(username=username)
	if len(user) > 0:
		# if user exists, check password
		isPassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
		if isPassword:
			request.session['id'] = user[0].id
			return redirect('/dashboard')
		else:
			messages.error(request, "Incorrect username/password combination.")
			return redirect('/')
	else:
		messages.error(request, "User does not exist.")
		return redirect('/')

	return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def jointrip(request,trip_id):
    new_trip = Trip.objects.get(id=trip_id)
    user = User.objects.get(id = request.session['id'])
    user.trips.add(new_trip)
    GoingonTrip.objects.create(trip=new_trip,user=user)
    return redirect('/dashboard')

def destination(request,trip_id):
    trip_details = Trip.objects.get(id=trip_id)
    trip_buddy = Trip.objects.filter(id=trip_id)
    trip_buddy = GoingonTrip.objects.filter(trip=trip_id) #,user=user)# going to add goingontrip model
    context={
        'trip_details':trip_details,
        'trip_buddy':trip_buddy
    }
    print trip_buddy
    return render(request,'main/destination.html',context)




    
