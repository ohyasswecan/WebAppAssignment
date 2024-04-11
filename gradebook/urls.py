from django.contrib.auth import admin
from django.urls import path

from gradebook import views
from gradebook.views import ClassEnrollmentListView, ClassEnrollmentDetailView, CourseListView, CourseDetailView, \
    EnrollmentDetailView, EnrollmentListView, LecturerListView, LecturerDetailView, SemesterListView, \
    SemesterDetailView, StudentListView, StudentDetailView

urlpatterns = [
    path('', views.home_views, name='home'),
    path('CourseList/', CourseListView.as_view(), name='courselist'),
    path('CourseList/CourseDetail/<int:pk>/', CourseDetailView.as_view(), name='coursedetail'),
    path('ClassList/', ClassEnrollmentListView.as_view(), name='classlist'),
    path('ClassList/ClassDetail/<int:pk>/', ClassEnrollmentDetailView.as_view(), name='classdetail'),
    path('SemesterList/', SemesterListView.as_view(), name='semesterlist'),
    path('SemesterList/SemesterDetail/<int:pk>', SemesterDetailView.as_view(), name='semesterdetail'),
    path('StudentList/', StudentListView.as_view(), name='studentlist'),
    path('StudentList/StudentDetail/<int:pk>', StudentDetailView.as_view(), name='studentdetail'),
    path('LecturerList/', LecturerListView.as_view(), name='lecturerlist'),
    path('LecturerList/LecturerDetail/<int:pk>/', LecturerDetailView.as_view(), name='lecturerdetail'),
    path('EnrollmentList/', EnrollmentListView.as_view(), name='enrollmentlist'),
    path('EnrollmentList/EnrollmentDetail/<int:student_id>/<int:class_id>/', EnrollmentDetailView.as_view(), name='enrollmentdetail')
]