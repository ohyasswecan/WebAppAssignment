from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, DetailView

from gradebook.models import Class_Enrollment, Course, Semester, Student, Lecturer, Student_Enrollment


# Create your views here.
def base_reflex(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def home_views(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
#template view version code
# def class_list_views(request):
#     class_list = Class_Enrollment.objects.all()
#     template = loader.get_template('ClassList.html')
#     context = {
#         'class_list': class_list
#     }
#     return HttpResponse(template.render(context, request))

class ClassEnrollmentListView(ListView):
    model = Class_Enrollment
    paginate_by = 20  # only show 20 items per page
    template_name = 'ClassList.html'
    ordering = ['class_id'] #Order by class_id field
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#Template view version class view
# def generic_details_views(request, class_id):
#     class_obj = Class_Enrollment.objects.get(pk=class_id)
#     return render(request, 'ClassDetailPage.html', {'class_obj': class_obj})

class ClassEnrollmentDetailView(DetailView):
    model = Class_Enrollment
    template_name = 'ClassDetailPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
#Template view version course list view
# def course_list_views(request):
#     course_list = Course.objects.all()
#     template = loader.get_template('CourseList.html')
#     context = {
#         'course_list': course_list
#     }
#     return HttpResponse(template.render(context, request))

class CourseListView(ListView):
    model = Course
    template_name = 'CourseList.html'
    ordering = ['course_id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'CourseDetailPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#Tempalte version semester list view
# def semester_list_views(request):
#     semester_list = Semester.objects.all()
#     template = loader.get_template('SemesterList.html')
#     context = {
#         'semester_list':semester_list
#     }
#     return HttpResponse(template.render(context,request))

class SemesterListView(ListView):
    model = Semester
    template_name = 'SemesterList.html'
    ordering = ['semester_id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SemesterDetailView(DetailView):
    model = Semester
    template_name = 'SemesterDetailPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#Template Version student list view
# def student_list_views(request):
#     student_list = Student.objects.all()
#     template = loader.get_template('StudentList.html')
#     context = {
#         'student_list':student_list
#     }
#     return HttpResponse(template.render(context, request))

class StudentListView(ListView):
    model = Student
    template_name = 'StudentList.html'
    ordering = ['student_id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'StudentDetailPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#Template version lecturer list view
# def lecturer_list_views(request):
#     lecturer_list = Lecturer.objects.all()
#     template = loader.get_template('LecturerList.html')
#     context = {
#         'lecturer_list':lecturer_list
#     }
#     return HttpResponse(template.render(context, request))

class LecturerListView(ListView):
    model = Lecturer
    template_name = 'LecturerList.html'
    ordering = ['staff_id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LecturerDetailView(DetailView):
    model = Lecturer
    template_name = 'LecturerDetailPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#Template version student enrollment list view
# def enrollment_list_views(request):
#     enrollment_list = Student_Enrollment.objects.all()
#     template = loader.get_template('EnrollmentList.html')
#     context = {
#         'enrollment_list':enrollment_list
#     }
#     return HttpResponse(template.render(context, request))

class EnrollmentListView(ListView):
    model = Student_Enrollment
    template_name = 'EnrollmentList.html'
    ordering = ['-enrollment_date'] #most recent enrolled student to most early enrolled student


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EnrollmentDetailView(DetailView):
    model = Student_Enrollment
    template_name = 'EnrollmentDetailPage.html'

    def get_object(self, queryset=None):
        student_id = self.kwargs.get('student_id')
        class_id = self.kwargs.get('class_id')
        queryset = self.get_queryset() #query filling  #queryset().filter(field1 = value1) to search by field value
        return queryset.get(student_id=student_id, class_id=class_id)#composite key query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



