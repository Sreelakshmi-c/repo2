from django.urls import path
from .import views
urlpatterns=[
    path('myapp/',views.fnHome,name='myapp'),
    path('index/',views.fnIndex,name='index/')
]