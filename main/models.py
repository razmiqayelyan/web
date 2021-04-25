from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Booking(models.Model):

	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	date_now = models.DateTimeField(auto_now_add=True)
	book_time = models.	CharField(unique=True,max_length=19)
	name = models.CharField('Name', max_length=50)
	employer = models.CharField(max_length=50, null=True)
	comment = models.CharField(max_length=222, null=True)
    
	def __str__(self):
		return f'*Name:{self.name}*____ *Book With:{self.employer}*____ *Booking Date:{self.book_time}*'

	def get_absolute_url(self):
		return f'/{self.user.username}'