from django.urls import path
from . import views
from .views import ActivityListView,activitydetail,loadteacheractivity

urlpatterns=[
    path('home/',views.home,name='activity-home'),
    #path('create/',ActivityCreateView.as_view(template_name='activity/post_form.html'),name='activity-create'),
    path('create/',views.createActivity,name='activity-create'),
    path('listview/',ActivityListView.as_view(template_name='activity/home.html'),name='activity-list'),
    path('teacher-activity/',loadteacheractivity,name='teacher-activity'),
    path('detailview/<int:id>/',views.activitydetail,name='activity-detail'),
    path('all-students/',views.display_all_students,name='all-students'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('student-dashboard/',views.student_dashboard,name='student-dashboard'),
    path('student-score-card/',views.display_score_card,name='student-score-card'),
    # path('activity-accept-confirmation/',views.activity_accept_confirm,name='activity-accept-form'),
    path('about/',views.about,name='activity-about'),
    path('display-students-table/',views.display_students_table,name='display-students-table')
]