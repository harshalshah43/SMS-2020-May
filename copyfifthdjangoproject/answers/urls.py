from django.urls import path
from . import views

urlpatterns =[
    # path('answers-list/',views.answers_list,name='answer-list'),
    path('submit-answer/<int:id>/',views.create_answer,name='submit-answer'),
    path('mysubmissions/',views.mysubmissions,name='mysubmissions'),
    path('student-answers-list/',views.loadstudentanswers,name='student-answer-list'),
    path('student-pending-answers-list/<int:id>/',views.loadpendingstudentanswersbyteachers,name='student-pending-answer-list'),
    path('student-rejected-answers-list/<int:id>/',views.loadrejectedstudentanswersbyteachers,name='student-rejected-answer-list'),
    path('student-answers-list-by-teachers/<int:id>/',views.loadstudentanswersbyteachers,name='student-answer-list-by-teachers'),
    path('activity-answers-list/<int:id>/',views.loadactivityanswers,name='activity-answer-list'),
    path('answer-detail/<int:id>',views.answerdetail,name='answer-detail'),
    path('answer-accept/<int:id>/',views.acceptanswer,name='accept-answer'),
    path('reject-accept/<int:id>/',views.rejectanswer,name='reject-answer'),

]