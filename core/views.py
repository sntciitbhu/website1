from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from pyrebase import pyrebase
from django.contrib import auth
import requests

config = {
'apiKey': "AIzaSyAkdfqj13ozWerQi0N6DFDEmAoc92laxvk",
'authDomain': "fir-1-d4538.firebaseapp.com",
'databaseURL': "https://fir-1-d4538.firebaseio.com",
'projectId': "fir-1-d4538",
'storageBucket': "fir-1-d4538.appspot.com",
'messagingSenderId': "570404350925"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

#############
#Signin Views
#############
def signin(request):
	return render(request, 'signin.html')

def postsign(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user = auth.sign_in_with_email_and_password(email,password)
		except:
			message = "Invalid Credentials"
			return render(request, 'signin.html', {'msg': message})
		print(user['idToken'])
		print(user)
		session_id = user['idToken']
		request.session['uid'] = str(session_id)

		#return render(request, 'mypage.html', {'e': email})
		return redirect(index, email=email, user=user['localId'] )
	message = "Not Allowed, you need to login first."
	return render(request, 'signin.html', {'msg': message})


#Logout View
def logout(request):
	auth.logout(request)
	return render(request, 'signin/')

#Trash
def index(request, email, user=""):
	#print(auth.current_user)
	#print(user.is_authenticated)
	#print(user)
	return render(request, 'mypage.html', { 'email': email, 'user':user })

#####################
#Password Reset Views
#####################
def resetpassword(request):
	return render(request, 'reset_password.html')

def postresetpassword(request):
	if request.method == "POST":
		email = request.POST.get('email')
		try:
			auth.send_password_reset_email(email)
		except:
			message = "Invalid email"
			return render(request, 'reset_password.html', {'msg': message})
		message = "Password reset link send to your email."
		return render(request, 'signin.html', {'msg': message})
	message = "Better luck next time"
	return render(request, 'signin.html', {'msg': message})

#
#Sign Up views
#
def signup(request):
	if request.method=="POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('pass')
		if email[-11:]=="itbhu.ac.in" or email[-12:]=="itbhu.ac.in ":
			try:
				user = auth.create_user_with_email_and_password(email, password)
				uid = user['localId']
				data = {'name':name, 'status': 1}
				database.child('users').child(uid).child('details').set(data)	
			except requests.exceptions.HTTPError as e :
				#message = "Unable to create account, sorry :-()"
				message = e.args[1]
				error = json.loads(message)['error']
				#error = str(error)
				#error = error.replace('&#39;',"'")
				return render(request, 'signup.html', {'msg': error['message'] })
			#return render(request, 'signin.html', {'msg': "Signup success :-))"})
			return redirect(postsignup)
		else:
			return render(request, 'signup.html', {'msg': "@itbhu.ac.in email required"})
	return render(request, 'signup.html')
import json
def postsignup(request):
	'''if request.method=="POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('pass')
		if email[-11:]=="itbhu.ac.in" or email[-12:]=="itbhu.ac.in ":
			try:
				user = auth.create_user_with_email_and_password(email, password)
				uid = user['localId']
				data = {'name':name, 'status': 1}
				database.child('users').child(uid).child('details').set(data)	
			except requests.exceptions.HTTPError as e :
				#message = "Unable to create account, sorry :-()"
				message = e.args[1]
				error = json.loads(message)['error']
				#error = str(error)
				#error = error.replace('&#39;',"'")
				return render(request, 'signup.html', {'msg': error['message'] })
			return render(request, 'signin.html', {'msg': "Signup success :-))"})
		else:
			return render(request, 'signup.html', {'msg': "@itbhu.ac.in email required"})'''
	return render(request, 'postsignup.html')
	
#
#Activity views	
#
def addactivity(request):
	render(request, 'addactivity.html')












#Regular views
def home(request):
    return render(request, 'index.html')

def amc(request):
	return render(request, 'amc.html', {})

def astro(request):
	return render(request, 'astro.html', {})

def cops(request):
	return render(request, 'cops.html', {})

def csi(request):
	return render(request, 'csi.html', {})

def robotics(request):
	return render(request, 'robotics.html', {})

def sae(request):
	return render(request, 'sae.html', {})

def biz(request):
	return render(request, 'biz.html', {})

def team(request):
	return render(request, 'team.html', {})

def certificates(request):
        return render(request, 'certificates.html', {})

def inventory(request):
        return render(request, 'tac.html', {})

def learning(request):
        return render(request, 'learning.html', {})

def udaan(request):
        return render(request, 'udaan.html', {})

def verification(request):
        return render(request, 'verification.html', {})

def blog(request):
        return render(request, 'blog.html', {})

def app(request):
	return HttpResponseRedirect("https://play.google.com/store/apps/details?id=in.shriyansh.questify&hl=en")

