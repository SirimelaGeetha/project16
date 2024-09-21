from django.urls import path 
from travel.views import *

app_name= 'travelling'
urlpatterns=[
    path('cake/',cake,name='cake')
]