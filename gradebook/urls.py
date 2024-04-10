from django.contrib.auth import admin
from django.urls import path

from gradebook import views
from gradebook.views import ClassEnrollmentListView, ClassEnrollmentDetailView

urlpatterns = [
    path('', views.home_views, name='home'),
    path('CourseList/', views.course_list_views, name='courselist'),
    path('ClassList/', ClassEnrollmentListView.as_view(), name='classlist'),
    path('ClassList/ClassDetail/<int:pk>/', ClassEnrollmentDetailView.as_view(), name='classdetail'),
    path('SemesterList/', views.semester_list_views, name='semesterlist'),
    path('StudentList/', views.student_list_views, name='studentlist'),
    path('LecturerList/', views.lecturer_list_views, name='lecturerlist'),
    path('EnrollmentList/', views.enrollment_list_views, name='enrollmentlist'),
]