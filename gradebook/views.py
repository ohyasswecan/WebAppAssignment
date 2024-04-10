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
def course_list_views(request):
    course_list = Course.objects.all()
    template = loader.get_template('CourseList.html')
    context = {
        'course_list': course_list
    }
    return HttpResponse(template.render(context, request))

def semester_list_views(request):
    semester_list = Semester.objects.all()
    template = loader.get_template('SemesterList.html')
    context = {
        'semester_list':semester_list
    }
    return HttpResponse(template.render(context,request))

def student_list_views(request):
    student_list = Student.objects.all()
    template = loader.get_template('StudentList.html')
    context = {
        'student_list':student_list
    }
    return HttpResponse(template.render(context, request))

def lecturer_list_views(request):
    lecturer_list = Lecturer.objects.all()
    template = loader.get_template('LecturerList.html')
    context = {
        'lecturer_list':lecturer_list
    }
    return HttpResponse(template.render(context, request))

def enrollment_list_views(request):
    enrollment_list = Student_Enrollment.objects.all()
    template = loader.get_template('EnrollmentList.html')
    context = {
        'enrollment_list':enrollment_list
    }
    return HttpResponse(template.render(context, request))





