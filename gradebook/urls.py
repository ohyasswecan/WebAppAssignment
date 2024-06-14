from django.contrib.auth import admin
from django.urls import path, include

from gradebook import views
from rest_framework.routers import DefaultRouter
from gradebook.views import ClassEnrollmentListView, ClassEnrollmentDetailView, CourseListView, CourseDetailView, \
    EnrollmentDetailView, EnrollmentListView, LecturerListView, LecturerDetailView, SemesterListView, \
    SemesterDetailView, StudentListView, StudentDetailView
from .views import (CourseViewSet, SemesterViewSet, LecturerViewSet,
                    StudentViewSet, ClassEnrollmentViewSet, StudentEnrollmentViewSet)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'students', StudentViewSet)
router.register(r'class_enrollments', ClassEnrollmentViewSet)
router.register(r'student_enrollments', StudentEnrollmentViewSet)

urlpatterns = [
    path('', views.home_views, name='home'),
    path('api/', include(router.urls)),
    path('UserProfile/', views.update_userprofile_views, name='update_userprofile'),
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
    path('StudentList/UploadStudentList/', views.upload_excel, name='uploadstudentlist'),
    path('StudentList/InsertStudentList/', views.insert_list, name='insertstudentlist'),
    path('StudentList/CreateStudent/', views.create_student_views, name='createstudent'),
    path('StudentList/StudentDetail/UpdateStudent/<int:student_id>/',views.update_student_views, name='updatestudent'),
    path('StudentList/StudentDetail/DeleteStudent/<int:student_id>', views.delete_student_views, name='deletestudent'),
    path('StudentList/StudentDetail/<int:pk>', StudentDetailView.as_view(), name='studentdetail'),
    path('LecturerList/', LecturerListView.as_view(), name='lecturerlist'),
    path('LecturerList/CreateLecturer/', views.create_lecturer_views, name='createlecturer'),
    path('LecturerList/LecturerDetail/UpdateLecturer/<int:staff_id>', views.update_lecturer_views, name='updatelecturer'),
    path('LecturerList/LecturerDetail/DeleteLecturer/<int:staff_id>', views.delete_lecturer_views, name='deletelecturer'),
    path('LecturerList/LecturerDetail/<int:pk>/', LecturerDetailView.as_view(), name='lecturerdetail'),
    path('EnrollmentList/', EnrollmentListView.as_view(), name='enrollmentlist'),
    path('EnrollmentList/CreateEnrollment/', views.create_studentenrollment_views, name='createstudentenrollment'),
    path('EnrollmentList/EnrollmentDetail/UpdateEnrollment/<int:student_id>/<int:class_id>/', views.update_studentenrollment_views, name='updatestudentenrollment'),
    path('EnrollmentList/EnrollmentDetail/DeleteEnrollment/<int:student_id>/<int:class_id>/', views.delete_studentenrollment_views, name='deletestudentenrollment'),
    path('EnrollmentList/EnrollmentDetail/<int:student_id>/<int:class_id>/', EnrollmentDetailView.as_view(), name='enrollmentdetail'),
]