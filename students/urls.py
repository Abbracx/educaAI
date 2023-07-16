from django.urls import path, include
from . import views 

urlpatterns = [
    path('register/', views.StudentRegistrationView.as_view(), 
         name='student_registration'),
         path('students/', include('students.urls')),
    path('enroll-course/',
        views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'),
]