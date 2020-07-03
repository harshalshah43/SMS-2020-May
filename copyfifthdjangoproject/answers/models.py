from django.db import models
from activity.models import Activity
from users.models import StudentProfile,TeacherProfile
from django.utils import timezone

class Answer(models.Model):
    title=models.CharField(max_length=50)
    course=models.CharField(max_length=30,default=None)
    subject=models.CharField(max_length=30)
    assignment=models.ForeignKey(Activity,on_delete=models.CASCADE)
    author =models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    pdf=models.FileField(default='sample.pdf',upload_to='answers')
    content=models.TextField(default='Content Here')
    date_posted=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,default='Pending')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
 	    return reverse('submit-answer',kwargs={'pk':self.pk})

class Marks(models.Model):
    student =models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    answer  =models.ForeignKey(Answer,on_delete=models.CASCADE)
    activity=models.ForeignKey(Activity,on_delete=models.CASCADE)
    scored =models.IntegerField(default=0)
    OutOf  =models.IntegerField(default=10)

   
    

