from django.urls import path
from . import views 
urlpatterns=[
    path('register/',views.teacherregister,name ='teacher-register'),
    
]
