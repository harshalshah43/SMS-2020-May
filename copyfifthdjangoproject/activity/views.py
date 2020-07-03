from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (ListView,
                                DetailView,CreateView,
                                UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Activity
from answers.models import Answer
from django.contrib.auth.models import User
from users.models import TeacherProfile,StudentProfile
from .forms import ActivityCreateForm
from django.contrib.auth.decorators import login_required

def home(request):
	# data=[
	# 	{
	# 	'title':'Post1',
	# 	'content':'My first Post',
	# 	'author':'Harshal',
    #     'date_posted':'October 25th, 2019',
    #     'currently_active':True
	# 	},
	# 	{
	# 		'title':'Post2',
	# 		'content':'My Second Post',
	# 		'author':'Saatvik',
    #         'date_posted':'October 26th, 2019',
    #         'currently_active':False
	# 	}
	
	# ]
        context={
                
            'title':'Harshal',
            'posts':Activity.objects.all(),
            }
        if request.method=='GET':
            object=TeacherProfile.objects.filter(teacher=request.user.id).first()
            object2=StudentProfile.objects.filter(student=request.user.id).first()
            if object is not None:
                context={
                        'title':'Harshal',
                        'posts':Activity.objects.all().order_by('-date_posted'),
                        'teacher_is_staff':object.is_staff,
                        
                        }
            elif object2 is not None:
                context={
                        'title':'Harshal',
                        'posts':Activity.objects.all().order_by('-date_posted'),
                        'student_is_current_student':object2.is_current_student,
                        
                        }
        else:
            context={
            'title':'Harshal',
            'posts':Activity.objects.all().order_by('-date_posted'),
            }
        return render(request,'activity/home.html',context)
	    
def display_all_students(request):
    object=TeacherProfile.objects.filter(teacher=request.user.id).first()
    object2=StudentProfile.objects.filter(student=request.user.id).first()
    
    context={
            'title':'Harshal',
            'posts':StudentProfile.objects.all(),
            'teacher_is_staff':object.is_staff,
                        
            }
    
    return render(request,'activity/all_students.html',context)

def display_students_table(request):
    teacher=TeacherProfile.objects.filter(teacher=request.user.id).first()
    context={
        'title':'Harshal',
        'posts':StudentProfile.objects.all(),
        'teacher_is_staff':teacher.is_staff
    }
    return render(request,'activity/students_table.html',context)

def display_score_card(request):
    user_id=request.user.id
    object=StudentProfile.objects.filter(student=user_id)
    current_student=object.first()
    answers=Answer.objects.filter(author=current_student)
    current_student=StudentProfile.objects.filter(student=user_id).first()
    context={
        'title':'Harshal',
        'answers':answers,
        'student_is_current_student':current_student.is_current_student
    }
    return render(request,'answers/score_card.html',context)

@login_required
def dashboard(request):
    object=TeacherProfile.objects.filter(teacher=request.user.id).first()
    context={
            'title':'Harshal',
            'posts':StudentProfile.objects.all(),
            'teacher_is_staff':object.is_staff,
                        
            }
    return render(request,'activity/dashboard.html',context)

@login_required
def student_dashboard(request):
    object=StudentProfile.objects.filter(student=request.user.id).first()
    context={
            'title':'Harshal',
            'posts':StudentProfile.objects.all(),
            'student_is_current_student':object.is_current_student,
                        
            }
    return render(request,'activity/student_dashboard.html',context)



class ActivityListView(ListView):
	model=Activity
	template_name='activity/home.html'
	context_object_name='posts'
	ordering=['-date_posted']

@login_required
def createActivity(request):
    if request.method=='POST':
        #print('Recieving Post data.........')
        form=ActivityCreateForm(request.POST,request.FILES)
        user_id=request.user.id
        object=TeacherProfile.objects.filter(teacher=user_id).first()
        form.instance.author=object
        
        if form.is_valid():
            #print("Breakpoint inside form.is_valid ")
            form.save()
            context={
            'title':'Harshal',
            'posts':Activity.objects.all(),
            'teacher_is_staff':object.is_staff,
            }
            return render(request,'activity/home.html',context)
        #else : print("Data didn't validate")
    else:
        form =ActivityCreateForm()
    object=TeacherProfile.objects.filter(teacher=request.user.id).first()
    return render(request,'activity/activity_form.html',{'form':form,'teacher_is_staff':object.is_staff})

# class ActivityCreateView(LoginRequiredMixin,CreateView):
#     model=Activity
#     fields=['title','content','date_posted','expires_on','pdf']
#     template_name='activity/post_form.html'
#     def form_valid(self,form):   
#         #we are overriding the form valid method 
#         #assign the current logged in user as author 
#         user_id=self.request.user.id
#         object=TeacherProfile.objects.filter(teacher=user_id).first()
#         form.instance.author=object
#         return super().form_valid(form)
  
def activitydetail(request,id):
    aid=id
    currentactivity=Activity.objects.filter(id=aid).first()
    object=TeacherProfile.objects.filter(teacher=request.user.id).first()
    object2=StudentProfile.objects.filter(student=request.user.id).first()
    if object is not None:
                context={
                        'title':'Harshal',
                        'posts':Activity.objects.all(),
                        'teacher_is_staff':object.is_staff,
                        'object':currentactivity
                        }
    elif object2 is not None:
                context={
                        'title':'Harshal',
                        'posts':Activity.objects.all(),
                        'student_is_current_student':object2.is_current_student,
                        'object':currentactivity
                        }
    return render(request,'activity/activity_detail.html',context)

def loadteacheractivity(request):
    user_id=request.user.id
    object=TeacherProfile.objects.filter(teacher=user_id)
    current_teacher=object.first()
    activity_list=Activity.objects.filter(author=current_teacher)
    return render(request,'activity/useractivitylist.html',{'posts':activity_list,'teacher_is_staff':current_teacher.is_staff})           

class UserActivityListView(ListView):
    model=Activity
    template_name='activity/useractivitylist.html'  #<app>/<model>_<viewtype>.html
    context_object_name='object'
    #in our home template we have a object 'posts' through which we would be looping over 
    #by default in our class we have something called 'object_list' instead of posts and we need to fix that
    #ordering=['-date_posted'] #newer to oldest 
    

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        
        return Activity.objects.filter(author=user).order_by('-date_posted')


def about(request):
    return render(request,'activity/about.html')

def activity_accept_confirm(request):
	return render(request,'activity/activity_accept_confirmation.html')

