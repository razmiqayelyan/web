from django.forms import ModelForm ,TextInput
from .models import Booking

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = ['name','employer','comment','book_time']

		widgets = {
		'name': TextInput(attrs={
			'class':'form-control',
			'placeholder':'Full Name'
			}),
		'employer': TextInput(attrs={
			'class':'form-control',
			'placeholder':"Employee's Name"
			}),
		'comment': TextInput(attrs={
			'class':'form-control',
			'placeholder':'Comments'
			}),
		'book_time': TextInput(attrs={
			'class':'form-control',
			'placeholder':'Month/Day/Year Hours:Minutes'
			})
		}