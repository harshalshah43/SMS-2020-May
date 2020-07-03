from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager 
from django.utils import timezone 
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class TeacherProfile(models.Model):
    teacher=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpeg',upload_to='teacher_profile_pics')
    qualification=models.CharField(max_length=255,null=True,default=None)
    assigned_course=models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.teacher.username} Profile'
    

def create_teacherprofile(sender,instance,created,**kwargs):
    if created:
        TeacherProfile.objects.create(teacher=instance)
        print("Teacher Profile Created")


class StudentProfile(models.Model):
    student =models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpeg',upload_to='student_profile_pics')
    year=models.CharField(max_length=60)
    branch=models.CharField(max_length=60)
    assignments_accepted=models.IntegerField(default=0)
    assignments_rejected=models.IntegerField(default=0)
    is_current_student =models.BooleanField(default=True)
    
    def __str__(self):
        return self.student.username


def create_studentprofile(sender,instance,created,**kwargs):
    if created:
        StudentProfile.objects.create(student=instance)
        print("Student Profile Created")


# post_save.connect(create_teacherprofile,sender=User)
# post_save.connect(create_studentprofile,sender=User)