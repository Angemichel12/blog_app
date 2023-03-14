from django.urls import path
from . views import home,about,contact,login,readmore,addblog

urlpatterns = [
    path('', home, name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('readmore/',readmore,name='readmore'),
    path('addblog/',addblog,name='addblog'),
]
