from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.generic import ListView, DetailView

from gradebook.forms import Class_EnrollmentForm, CourseForm, SemesterForm, StudentForm, LecturerForm, \
    StudentEnrollmentForm, RegisterForm
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

def create_class_views(request):
    if request.method == 'POST':
        form = Class_EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classlist')
    else:
        form = Class_EnrollmentForm()
        return render(request, 'CreateInstanceForm.html', {'form': form,'object_list':Student_Enrollment.objects.all()})

def update_class_views(request, class_id):
    class_enrol = get_object_or_404(Class_Enrollment, pk=class_id)
    if request.method == 'POST':
        form = Class_EnrollmentForm(request.POST, instance=class_enrol)
        if form.is_valid():
            form.save()
            return redirect('classlist')
    else:
        form = Class_EnrollmentForm(instance=class_enrol)
        return render(request, 'UpdateInstanceForm.html', {'form': form,'object': class_enrol})

def delete_class_views(request, class_id):
    class_enrol = get_object_or_404(Class_Enrollment, pk=class_id)
    if request.method == 'POST':
        class_enrol.delete()
        return redirect('classlist')
    else:
        form = Class_EnrollmentForm(instance=class_enrol)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': class_enrol})

def create_course_views(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courselist')
    else:
        form = CourseForm()
        return render(request, 'CreateInstanceForm.html', {'form': form,'object_list':Course.objects.all()})

def update_course_views(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courselist')
    else:
        form = CourseForm(instance=course)
        return render(request, 'UpdateInstanceForm.html', {'form': form, 'object': course})

def delete_course_views(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courselist')
    else:
        form = Class_EnrollmentForm(instance=course)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': course})


def create_semester_views(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semesterlist')
    else:
        form = SemesterForm()
        return render(request, 'CreateInstanceForm.html', {'form': form,'object_list':Semester.objects.all()})


def update_semester_views(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('semesterlist')
    else:
        form = SemesterForm(instance=semester)
        return render(request, 'UpdateInstanceForm.html', {'form': form, 'object': semester})

def delete_semester_views(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)
    if request.method == 'POST':
        semester.delete()
        return redirect('semesterlist')
    else:
        form = SemesterForm(instance=semester)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': semester})


def create_student_views(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form = StudentForm()
        return render(request, 'CreateInstanceForm.html', {'form': form,'object_list':Student.objects.all()})


def update_student_views(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form = StudentForm(instance=student)
        return render(request, 'UpdateInstanceForm.html', {'form': form, 'object': student})

def delete_student_views(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('studentlist')
    else:
        form = StudentForm(instance=student)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': student})


def create_lecturer_views(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturerlist')
    else:
        form = LecturerForm()
        return render(request, 'CreateInstanceForm.html', {'form': form,'object_list':Lecturer.objects.all()})

def update_lecturer_views(request, staff_id):
    lecturer = get_object_or_404(Lecturer, pk=staff_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturerlist')
    else:
        form = LecturerForm(instance=lecturer)
        return render(request, 'UpdateInstanceForm.html', {'form': form, 'object': lecturer})

def delete_lecturer_views(request, staff_id):
    lecturer = get_object_or_404(Lecturer, pk=staff_id)
    if request.method == 'POST':
        lecturer.delete()
        return redirect('lecturerlist')
    else:
        form = LecturerForm(instance=lecturer)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': lecturer})

def create_studentenrollment_views(request):
    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollmentlist')
    else:
        form = StudentEnrollmentForm()
        return render(request, 'CreateInstanceForm.html', {'form': form,'object_list':Student_Enrollment.objects.all()})

def update_studentenrollment_views(request, student_id, class_id):
    student_enrol = get_object_or_404(Student_Enrollment, student_id=student_id, class_id=class_id)
    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST, instance=student_enrol)
        if form.is_valid():
            form.save()
            return redirect('enrollmentlist')
    else:
        form = StudentEnrollmentForm(instance=student_enrol)
        return render(request, 'UpdateInstanceForm.html', {'form': form, 'object': student_enrol})

def delete_studentenrollment_views(request, student_id, class_id):
    student_enrol = get_object_or_404(Student_Enrollment, student_id=student_id, class_id=class_id)
    if request.method == 'POST':
        student_enrol.delete()
        return redirect('enrollmentlist')
    else:
        form = StudentEnrollmentForm(instance=student_enrol)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': student_enrol})
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optionally log the user in directly
            return redirect('home')  # Redirect to a home page or other appropriate page
    else:
        form = RegisterForm()
    return render(request, 'registration/Register.html', {'form': form})