from django.urls import path 
from food.views import *

app_name= 'foodies'
urlpatterns=[
    path('chocolate/',chocolate,name='chocolate')
]