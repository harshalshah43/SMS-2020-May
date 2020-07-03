from django.shortcuts import render
from .forms import AnswerCreateForm
from users.models import StudentProfile,TeacherProfile
from .models import Answer,Marks
from activity.models import Activity
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.views.generic import (ListView,
#     DetailView,
#     CreateView,UpdateView,DeleteView,
#     )
# from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# def answers_list(request):
#     # answers=[{
#     #     'title':'title1',
#     #     'course':'DSA',
#     #     'subject':'DSA',
#     #     'assignment':'DSA',
#     # }]
#     answers_list=Answer.objects.all().filter(assignment=id)
#     context={
#         'answers':answers_list
#     }
#     return render(request,'answers/answers_list.html',context)

@login_required
def create_answer(request,id):
    user_id=request.user.id
    aid=id
    object=StudentProfile.objects.filter(student=user_id).first()
    current_activity=Activity.objects.all().filter(id=aid).first()
    if request.method=='POST':
        form =AnswerCreateForm(request.POST,request.FILES)
        user_id=request.user.id
        object=StudentProfile.objects.filter(student=user_id).first()
        current_activity=Activity.objects.all().filter(id=aid).first()
        form.instance.author=object
        form.instance.assignment=current_activity
        print(form)
        if form.is_valid():
            form.save()
            #print("form saved Breakpoint 1")
            answers_list=Answer.objects.all().filter(assignment=id)
            context={
            'answers':answers_list,
            'student_is_current_student':object.is_current_student
            }
            return render(request,'answers/answers_list.html',context)
        # else:
        #     #print('form was not saved')
        #     answers_list=Answer.objects.all().filter(assignment=id)
        #     context={
        #     'answers':answers_list
        #     }
        #     return render(request,'answers/answers_list.html',context)
    else:
        form=AnswerCreateForm()
        return render(request,'answers/submit_form.html',{'form':form,'title':'Harshal','student_is_current_student':object.is_current_student})

def mysubmissions(request):
    object=TeacherProfile.objects.filter(teacher=request.user.id).first()
    object2=StudentProfile.objects.filter(student=request.user.id).first()
    if object is not None:
        context={
            
            'teacher_is_staff':object.is_staff,
                }
    elif object2 is not None:
        context={
           
            'student_is_current_student':object2.is_current_student,
                }
    return render(request,'answers/mysubmissions.html',context)

# class StudentAnswersListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
#     model=Answer
#     template_name='answers/answers_list.html'
#     context_object_name='answers'
#     def get_queryset(self):
#         user=get_object_or_404(User,username=self.kwargs.get('username'))
       
#         return Answer.objects.filter(author=user)

# def studentanswerslist(request):
#     context={
#         'answers':Answer.objects.filter(author=request.user.id)
#     }
#     return render(request,'answers/answers_list.html/',context)
def answerdetail(request,id):
    aid=id
    answers=Answer.objects.filter(id=aid)
    object=TeacherProfile.objects.filter(teacher=request.user.id).first()
    object2=StudentProfile.objects.filter(student=request.user.id).first()
    if object is not None:
        context={
            'answers':answers,
            'teacher_is_staff':object.is_staff,
                }
    elif object2 is not None:
        context={
            'answers':answers,
            'student_is_current_student':object2.is_current_student,
                }
    return render(request,'answers/answers_list.html',context)
               

def loadactivityanswers(request,id):
    aid=id
    activity=Activity.objects.filter(id=aid).first()
    answers=Answer.objects.filter(assignment=activity)
    
    object=TeacherProfile.objects.filter(teacher=request.user.id).first()
    object2=StudentProfile.objects.filter(student=request.user.id).first()
    if object is not None:
        context={
            'answers':answers,
            'teacher_is_staff':object.is_staff,
                }
    elif object2 is not None:
        context={
            'answers':answers,
            'student_is_current_student':object2.is_current_student,
                }
    return render(request,'answers/activity_answers_list.html',context)

def loadstudentanswers(request):
    user_id=request.user.id
    object=StudentProfile.objects.filter(student=user_id)
    current_student=object.first()
    answers_list=Answer.objects.filter(author=current_student)
    return render(request,'answers/answers_list.html',{'answers':answers_list,'student_is_current_student':current_student.is_current_student})

def acceptanswer(request,id):
    tid=id
    messages.success(request,f'Answer has been accepted')

    loadstudentanswersbyteachers(request,tid)
    return render(request,'answers/answers_list.html',{'current_student':current_student})

def loadstudentanswersbyteachers(request,id):
    user_id=request.user.id
    sid=id
    current_student=StudentProfile.objects.filter(id=sid).first()
    current_teacher=TeacherProfile.objects.filter(id=user_id).first()
    answers_list=Answer.objects.filter(author=current_student)
    context={
            'answers':answers_list,
            'teacher_is_staff':current_teacher.is_staff,
                }
    return render(request,'answers/student_answers_list_byteachers.html',{'answers':answers_list,'current_student':current_student,'teacher_is_staff':current_teacher.is_staff})

def loadpendingstudentanswersbyteachers(request,id):
    user_id=request.user.id
    sid=id
    current_student=StudentProfile.objects.filter(id=sid).first()
    current_teacher=TeacherProfile.objects.filter(id=user_id).first()
    answers_list=Answer.objects.filter(author=current_student).filter(status='Pending')
    return render(request,'answers/student_answers_list_byteachers.html',{'answers':answers_list,'current_student':current_student,'teacher_is_staff':current_teacher.is_staff})

def loadrejectedstudentanswersbyteachers(request,id):
    user_id=request.user.id
    sid=id
    current_student=StudentProfile.objects.filter(id=sid).first()
    current_teacher=TeacherProfile.objects.filter(id=user_id).first()
    answers_list=Answer.objects.filter(author=current_student).filter(status='Rejected')
    return render(request,'answers/student_answers_list_byteachers.html',{'answers':answers_list,'current_student':current_student,'teacher_is_staff':current_teacher.is_staff})

def acceptanswer(request,id):
    #increasing the score 
    answer_id=id
    student = Answer.objects.filter(id=answer_id).first().author
    n=Answer.objects.filter(id=answer_id).first().author.assignments_accepted
    n+=1
    student.assignments_accepted=n
    answer =Answer.objects.filter(id=answer_id).first()
    answer.status='Accepted'
    act =answer.assignment
    st=answer.author
    marks =Marks(student =st,answer=answer,activity=act,scored =6)
    marks.save()
    answer.save()
    student.save()
    #end of update 
    context={
        'student':student,
        'assignments_accepted':student.assignments_accepted
    }
    return render(request,'answers/answer_accepted.html',context)

def rejectanswer(request,id):
    #increasing the score 
    answer_id=id
    student = Answer.objects.filter(id=answer_id).first().author
    n=Answer.objects.filter(id=answer_id).first().author.assignments_accepted
    n-=1
    student.assignments_accepted=n
    answer =Answer.objects.filter(id=answer_id).first()
    answer.status='Accepted'
    answer.save()
    student.save()
    #end of update 
    context={
        'student':student,
        'assignments_accepted':student.assignments_accepted
    }
    return render(request,'answers/answer_accepted.html',context)