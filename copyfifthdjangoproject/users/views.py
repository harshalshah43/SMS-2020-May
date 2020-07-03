from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import TeacherRegisterForm


def teacherregister(request):
    if request.method=='POST':
        form=TeacherRegisterForm(request.POST) #create a form instance with "POST" data
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            #firstname=form.cleaned_data.get('firstname')
            #print("firstname="+firstname)
            messages.success(request,f'Account Created for the {username}! and you are now able to login')
            return redirect('faculty-login')
    else:
        form=TeacherRegisterForm()   #create a blank form
    return render(request,'users/teacherregister.html',{'form':form })

    
