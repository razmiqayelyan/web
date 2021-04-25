from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from django.views.generic import UpdateView, DeleteView

# Create your views here.
def logout(request):
	auth.logout(request)
	return redirect('/')

def index(request):
	user = User.objects.all()
	return render(request, 'index.html')

class BookUpdateView(UpdateView):
	model = Booking
	template_name = 'bookingupdate.html'
	form_class = BookingForm
	context_object_name = 'book'

class BookDeleteView(DeleteView):
	model = Booking
	success_url = '/'
	template_name = 'delete.html'
	context_object_name = 'book'


	


def booking(request):
	error = ''
	if request.method == 'POST':
		form = BookingForm(request.POST or None)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.user = request.user;
			obj.save()
			form = BookingForm()

			return redirect('/')
		else:
			error = 'The Specified Time Has Already Been Booked'
	form = BookingForm()
	context = {'form':form,
				'error':error}
	return render(request, 'booking.html', context)

def profile(request, username):
	usera = User.objects.filter(username=username)
	book = Booking.objects.all() 
	context = {
	'usera' : usera,
	'book' : book
	}
	return render(request, 'profile.html', context)









def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Invalid Credentials')
			return redirect(login)

	else:
		return render(request, 'login.html')

def register(request):
	if request.method == 'POST':

		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username Taken')
				return redirect(register)
			else:
				user = User.objects.create_user(username=username, password=password1)
				user.save()
				messages.info(request, 'User Created')
				return redirect(login)
		else:
			messages.info(request, 'Password not matching...')
			return redirect(register)

	else:
		return render(request, 'register.html')