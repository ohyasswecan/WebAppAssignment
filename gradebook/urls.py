from django.contrib.auth import admin
from django.urls import path

from gradebook import views
from gradebook.views import ClassEnrollmentListView, ClassEnrollmentDetailView, CourseListView, CourseDetailView, \
    EnrollmentDetailView, EnrollmentListView, LecturerListView, LecturerDetailView, SemesterListView, \
    SemesterDetailView, StudentListView, StudentDetailView

urlpatterns = [
    path('', views.home_views, name='home'),
    path('CourseList/', CourseListView.as_view(), name='courselist'),
    path('CourseList/CreateCourse/', views.create_course_views, name='createcourse'),
    path('CourseList/CourseDetail/UpdateCourse/<int:course_id>/', views.update_course_views, name='updatecourse'),
    path('CourseList/CourseDetail/DeleteCourse/<int:course_id>/', views.delete_course_views, name='deletecourse'),
    path('CourseList/CourseDetail/<int:pk>/', CourseDetailView.as_view(), name='coursedetail'),
    path('ClassList/', ClassEnrollmentListView.as_view(), name='classlist'),
    path('ClassList/CreateClass/', views.create_class_views, name='createclass'),
    path('ClassList/ClassDetail/UpdateClass/<int:class_id>/',views.update_class_views, name='updateclass'),
    path('ClassList/ClassDetail/DeleteClass/<int:class_id>/',views.delete_class_views, name='deleteclass'),
    path('ClassList/ClassDetail/<int:pk>/', ClassEnrollmentDetailView.as_view(), name='classdetail'),
    path('SemesterList/', SemesterListView.as_view(), name='semesterlist'),
    path('SemesterList/CreateSemester/', views.create_semester_views, name='createsemester'),
    path('SemesterList/SemesterDetail/UpdateSemester/<int:semester_id>/',views.update_semester_views, name='updatesemester'),
    path('SemesterList/SemesterDetail/DeleteSemester/<int:semester_id>/',views.delete_semester_views, name='deletesemester'),
    path('SemesterList/SemesterDetail/<int:pk>', SemesterDetailView.as_view(), name='semesterdetail'),
    path('StudentList/', StudentListView.as_view(), name='studentlist'),
    path('StudentList/CreateStudent/', views.create_student_views, name='createstudent'),
    path('StudentList/StudentDetail/UpdateStudent/<int:student_id>/',views.update_student_views, name='updatestudent'),
    path('StudentList/StudentDetail/DeleteStudent/<int:student_id>', views.delete_student_views, name='deletestudent'),
    path('StudentList/StudentDetail/<int:pk>', StudentDetailView.as_view(), name='studentdetail'),
    path('LecturerList/', LecturerListView.as_view(), name='lecturerlist'),
    path('LecturerList/LecturerDetail/<int:pk>/', LecturerDetailView.as_view(), name='lecturerdetail'),
    path('EnrollmentList/', EnrollmentListView.as_view(), name='enrollmentlist'),
    path('EnrollmentList/EnrollmentDetail/<int:student_id>/<int:class_id>/', EnrollmentDetailView.as_view(), name='enrollmentdetail')
]