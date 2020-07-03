from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.utils.timezone import timedelta
from users.models import TeacherProfile
from django.urls import reverse

class Activity(models.Model):
    title=models.CharField(max_length=100)
    author =models.ForeignKey(TeacherProfile,on_delete=models.CASCADE)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    expires_on=models.DateTimeField(default=(timezone.now()+timedelta(days=1)))
    currently_active=models.BooleanField(default=True)
    pdf=models.FileField(default='sample.pdf',upload_to='assignments')
    activity_marks=models.IntegerField(default=10)

    def save(self, *args, **kwargs):
        if timezone.now() > expires_on:
            currently_active=False
        super().save(*args, **kwargs)
        


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
 	    return reverse('activity-list')

    