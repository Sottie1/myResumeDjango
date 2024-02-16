from django.urls import path
from myresume.views import *



app_name ='myresume'


urlpatterns = [
    path("", index, name="index"),
    
]
