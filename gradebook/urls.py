from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gradebook.views import (
    ClassEnrollmentListView, ClassEnrollmentDetailView,
    CourseListView, CourseDetailView,
    SemesterListView, SemesterDetailView,
    StudentListView, StudentDetailView,
    LecturerListView, LecturerDetailView,
    EnrollmentListView, EnrollmentDetailView,
    CreateClassView, UpdateClassView, DeleteClassView,
    CreateCourseView, UpdateCourseView, DeleteCourseView,
    CreateSemesterView, UpdateSemesterView, DeleteSemesterView,
    CreateStudentView, UpdateStudentView, DeleteStudentView,
    CreateLecturerView, UpdateLecturerView, DeleteLecturerView,
    CreateStudentEnrollmentView, UpdateStudentEnrollmentView, DeleteStudentEnrollmentView,
    RegisterView, UploadExcelView, InsertListView, UpdateUserProfileView,
    BaseReflexView, IndexView, HomeView,
    CourseViewSet, SemesterViewSet, LecturerViewSet, StudentViewSet, ClassEnrollmentViewSet, StudentEnrollmentViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'students', StudentViewSet)
router.register(r'class_enrollments', ClassEnrollmentViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('base/', BaseReflexView.as_view(), name='base'),
    path('api/', include(router.urls)),
    path('api/student_enrollments/', EnrollmentListView.as_view(), name='student_enrollment-list'),
    path('api/student_enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='student_enrollment-detail'),
    path('UserProfile/', UpdateUserProfileView.as_view(), name='update_userprofile'),
    path('CourseList/', CourseListView.as_view(), name='courselist'),
    path('CourseList/CreateCourse/', CreateCourseView.as_view(), name='createcourse'),
    path('CourseList/CourseDetail/UpdateCourse/<int:course_id>/', UpdateCourseView.as_view(), name='updatecourse'),
    path('CourseList/CourseDetail/DeleteCourse/<int:course_id>/', DeleteCourseView.as_view(), name='deletecourse'),
    path('CourseList/CourseDetail/<int:pk>/', CourseDetailView.as_view(), name='coursedetail'),
    path('ClassList/', ClassEnrollmentListView.as_view(), name='classlist'),
    path('ClassList/CreateClass/', CreateClassView.as_view(), name='createclass'),
    path('ClassList/ClassDetail/UpdateClass/<int:class_id>/', UpdateClassView.as_view(), name='updateclass'),
    path('ClassList/ClassDetail/DeleteClass/<int:class_id>/', DeleteClassView.as_view(), name='deleteclass'),
    path('ClassList/ClassDetail/<int:pk>/', ClassEnrollmentDetailView.as_view(), name='classdetail'),
    path('SemesterList/', SemesterListView.as_view(), name='semesterlist'),
    path('SemesterList/CreateSemester/', CreateSemesterView.as_view(), name='createsemester'),
    path('SemesterList/SemesterDetail/UpdateSemester/<int:semester_id>/', UpdateSemesterView.as_view(),
         name='updatesemester'),
    path('SemesterList/SemesterDetail/DeleteSemester/<int:semester_id>/', DeleteSemesterView.as_view(),
         name='deletesemester'),
    path('SemesterList/SemesterDetail/<int:pk>', SemesterDetailView.as_view(), name='semesterdetail'),
    path('StudentList/', StudentListView.as_view(), name='studentlist'),
    path('StudentList/UploadStudentList/', UploadExcelView.as_view(), name='uploadstudentlist'),
    path('StudentList/InsertStudentList/', InsertListView.as_view(), name='insertstudentlist'),
    path('StudentList/CreateStudent/', CreateStudentView.as_view(), name='createstudent'),
    path('StudentList/StudentDetail/UpdateStudent/<int:student_id>/', UpdateStudentView.as_view(),
         name='updatestudent'),
    path('StudentList/StudentDetail/DeleteStudent/<int:student_id>', DeleteStudentView.as_view(), name='deletestudent'),
    path('StudentList/StudentDetail/<int:pk>', StudentDetailView.as_view(), name='studentdetail'),
    path('LecturerList/', LecturerListView.as_view(), name='lecturerlist'),
    path('LecturerList/CreateLecturer/', CreateLecturerView.as_view(), name='createlecturer'),
    path('LecturerList/LecturerDetail/UpdateLecturer/<int:staff_id>', UpdateLecturerView.as_view(),
         name='updatelecturer'),
    path('LecturerList/LecturerDetail/DeleteLecturer/<int:staff_id>', DeleteLecturerView.as_view(),
         name='deletelecturer'),
    path('LecturerList/LecturerDetail/<int:pk>/', LecturerDetailView.as_view(), name='lecturerdetail'),
    path('EnrollmentList/', EnrollmentListView.as_view(), name='enrollmentlist'),
    path('EnrollmentList/CreateEnrollment/', CreateStudentEnrollmentView.as_view(), name='createstudentenrollment'),
    path('EnrollmentList/EnrollmentDetail/UpdateEnrollment/<int:student_id>/<int:class_id>/',
         UpdateStudentEnrollmentView.as_view(), name='updatestudentenrollment'),
    path('EnrollmentList/EnrollmentDetail/DeleteEnrollment/<int:student_id>/<int:class_id>/',
         DeleteStudentEnrollmentView.as_view(), name='deletestudentenrollment'),
    path('EnrollmentList/EnrollmentDetail/<int:student_id>/<int:class_id>/', EnrollmentDetailView.as_view(),
         name='enrollmentdetail'),
    path('register/', RegisterView.as_view(), name='register'),
]
