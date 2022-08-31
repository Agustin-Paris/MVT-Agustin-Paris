from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('Familiares/', Familiares, name= "Familiares"),
    path('', inicio),
    
]