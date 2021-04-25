from django.urls import path
from .views import *

urlpatterns = [
   path('', index, name='first_page'),
   path('login/', login, name='login'),
   path('register/', register, name='register'),
   path('logout/', logout, name='logout'),
   path('booking/', booking, name='booking'),
   path('<username>/', profile, name='profile'),
   path('<username>/<int:pk>', BookUpdateView.as_view(), name='update'),
   path('<username>/<int:pk>/delete', BookDeleteView.as_view(), name='delete'),

]