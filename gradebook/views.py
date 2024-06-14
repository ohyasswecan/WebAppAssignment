import pandas as pd
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.views.generic import ListView, DetailView
import datetime

from rest_framework import viewsets

from gradebook.forms import Class_EnrollmentForm, CourseForm, SemesterForm, StudentForm, LecturerForm, \
    StudentEnrollmentForm, RegisterForm, UploadExcelForm, UserProfileForm, CustomUserCreationForm
from gradebook.models import Class_Enrollment, Course, Semester, Student, Lecturer, Student_Enrollment, UserProfile
from .serializers import CourseSerializer, SemesterSerializer, LecturerSerializer, StudentSerializer, ClassEnrollmentSerializer, StudentEnrollmentSerializer

# Create your views here.
def base_reflex(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def home_views(request):
    return render(request, 'home.html')



# template view version code
# def class_list_views(request):
#     class_list = Class_Enrollment.objects.all()
#     template = loader.get_template('ClassList.html')
#     context = {
#         'class_list': class_list
#     }
#     return HttpResponse(template.render(context, request))

class ClassEnrollmentListView(LoginRequiredMixin,ListView):
    model = Class_Enrollment
    template_name = 'ClassList.html'
    ordering = ['class_id']  # Order by class_id field
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Class_EnrollmentForm()
        context['user'] = self.request.user
        return context


# Template view version class view
# def generic_details_views(request, class_id):
#     class_obj = Class_Enrollment.objects.get(pk=class_id)
#     return render(request, 'ClassDetailPage.html', {'class_obj': class_obj})

class ClassEnrollmentDetailView(LoginRequiredMixin,DetailView):
    model = Class_Enrollment
    template_name = 'ClassDetailPage.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Template view version course list view
# def course_list_views(request):
#     course_list = Course.objects.all()
#     template = loader.get_template('CourseList.html')
#     context = {
#         'course_list': course_list
#     }
#     return HttpResponse(template.render(context, request))

class CourseListView(LoginRequiredMixin,ListView):
    model = Course
    template_name = 'CourseList.html'
    ordering = ['course_id']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['form'] = CourseForm()
        return context


class CourseDetailView(LoginRequiredMixin,DetailView):
    model = Course
    template_name = 'CourseDetailPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Tempalte version semester list view
# def semester_list_views(request):
#     semester_list = Semester.objects.all()
#     template = loader.get_template('SemesterList.html')
#     context = {
#         'semester_list':semester_list
#     }
#     return HttpResponse(template.render(context,request))

class SemesterListView(LoginRequiredMixin,ListView):
    model = Semester
    template_name = 'SemesterList.html'
    ordering = ['semester_id']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['form'] = SemesterForm()
        return context


class SemesterDetailView(LoginRequiredMixin,DetailView):
    model = Semester
    template_name = 'SemesterDetailPage.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Template Version student list view
# def student_list_views(request):
#     student_list = Student.objects.all()
#     template = loader.get_template('StudentList.html')
#     context = {
#         'student_list':student_list
#     }
#     return HttpResponse(template.render(context, request))

class StudentListView(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'StudentList.html'
    ordering = ['student_id']
    paginate_by = 100


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        context['user'] = self.request.user
        return context


class StudentDetailView(LoginRequiredMixin,DetailView):
    model = Student
    template_name = 'StudentDetailPage.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Template version lecturer list view
# def lecturer_list_views(request):
#     lecturer_list = Lecturer.objects.all()
#     template = loader.get_template('LecturerList.html')
#     context = {
#         'lecturer_list':lecturer_list
#     }
#     return HttpResponse(template.render(context, request))

class LecturerListView(LoginRequiredMixin,ListView):
    model = Lecturer
    template_name = 'LecturerList.html'
    ordering = ['staff_id']
    paginate_by = 100


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LecturerForm()
        context['user'] = self.request.user
        return context


class LecturerDetailView(LoginRequiredMixin,DetailView):
    model = Lecturer
    template_name = 'LecturerDetailPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Template version student enrollment list view
# def enrollment_list_views(request):
#     enrollment_list = Student_Enrollment.objects.all()
#     template = loader.get_template('EnrollmentList.html')
#     context = {
#         'enrollment_list':enrollment_list
#     }
#     return HttpResponse(template.render(context, request))

class EnrollmentListView(LoginRequiredMixin,ListView):
    model = Student_Enrollment
    template_name = 'EnrollmentList.html'
    ordering = ['-enrollment_date']  # most recent enrolled student to most early enrolled student
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentEnrollmentForm()
        context['user'] = self.request.user
        return context


class EnrollmentDetailView(LoginRequiredMixin,DetailView):
    model = Student_Enrollment
    template_name = 'EnrollmentDetailPage.html'

    def get_object(self, queryset=None):
        student_id = self.kwargs.get('student_id')
        class_id = self.kwargs.get('class_id')
        queryset = self.get_queryset()  # query filling  #queryset().filter(field1 = value1) to search by field value
        return queryset.get(student_id=student_id, class_id=class_id)  # composite key query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

@login_required
def create_class_views(request):
    if request.method == 'POST':
        form = Class_EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classlist')
    else:
        form = Class_EnrollmentForm()
        return render(request, 'CreateInstanceForm.html',
                      {'form': form, 'object_list': Student_Enrollment.objects.all()})

@login_required
def update_class_views(request, class_id):
    class_enrol = get_object_or_404(Class_Enrollment, pk=class_id)
    if request.method == 'POST':
        form = Class_EnrollmentForm(request.POST, instance=class_enrol)
        if form.is_valid():
            form.save()
            return redirect('classlist')
    else:
        form = Class_EnrollmentForm(instance=class_enrol)
        return render(request, 'UpdateInstanceForm.html', {'form': form, 'object': class_enrol})

@login_required
def delete_class_views(request, class_id):
    class_enrol = get_object_or_404(Class_Enrollment, pk=class_id)
    if request.method == 'POST':
        class_enrol.delete()
        return redirect('classlist')
    else:
        form = Class_EnrollmentForm(instance=class_enrol)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': class_enrol})

@login_required
def create_course_views(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courselist')
    else:
        form = CourseForm()
        return render(request, 'CreateInstanceForm.html', {'form': form, 'object_list': Course.objects.all()})

@login_required
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

@login_required
def delete_course_views(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('courselist')
    else:
        form = Class_EnrollmentForm(instance=course)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': course})

@login_required
def create_semester_views(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semesterlist')
    else:
        form = SemesterForm()
        return render(request, 'CreateInstanceForm.html', {'form': form, 'object_list': Semester.objects.all()})

@login_required
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

@login_required
def delete_semester_views(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)
    if request.method == 'POST':
        semester.delete()
        return redirect('semesterlist')
    else:
        form = SemesterForm(instance=semester)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': semester})

@login_required
def create_student_views(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form = StudentForm()
        return render(request, 'CreateInstanceForm.html', {'form': form, 'object_list': Student.objects.all()})

@login_required
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

@login_required
def delete_student_views(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('studentlist')
    else:
        form = StudentForm(instance=student)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': student})

@login_required
def create_lecturer_views(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturerlist')
    else:
        form = LecturerForm()
        return render(request, 'CreateInstanceForm.html', {'form': form, 'object_list': Lecturer.objects.all()})

@login_required
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

@login_required
def delete_lecturer_views(request, staff_id):
    lecturer = get_object_or_404(Lecturer, pk=staff_id)
    if request.method == 'POST':
        lecturer.delete()
        return redirect('lecturerlist')
    else:
        form = LecturerForm(instance=lecturer)
        return render(request, 'DeleteInstanceForm.html', {'form': form, 'object': lecturer})

@login_required
def create_studentenrollment_views(request):
    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollmentlist')
    else:
        form = StudentEnrollmentForm()
        return render(request, 'CreateInstanceForm.html',
                      {'form': form, 'object_list': Student_Enrollment.objects.all()})

@login_required
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

@login_required
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optionally log the user in directly
            return redirect('home')  # Redirect to a home page or other appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/Register.html', {'form': form})

@login_required
def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            request.session['excel_data'] = df.to_dict(orient='records')
            df_html = df.to_html(classes='table table-striped')
            return render(request, "ExcelUploadStudentList.html",
                          {'form': form, 'df_html': df_html, 'show_insert_form': True})
    else:
        form = UploadExcelForm()
    return render(request, "ExcelUploadStudentList.html", {'form': form, 'show_insert_form': False})

@login_required
def insert_list(request):
    if request.method == 'POST':
        df_records = request.session.get('excel_data')

        if df_records:
            # Iterate over each row in the DataFrame
            for row in df_records:
                try:
                    # Convert date from MM/DD/YYYY to YYYY-MM-DD
                    formatted_date = datetime.datetime.strptime(row['student_DOB'], '%m/%d/%Y').date()
                    #skip the student from excel sheet when current student id duplicated with database record
                    obj, created = Student.objects.get_or_create(
                        student_id=row['student_id'],
                        defaults={
                            'student_firstname': row['student_firstname'],
                            'student_lastname': row['student_lastname'],
                            'student_email': row['student_email'],
                            'student_DOB': formatted_date
                        }
                    )
                    if not created:
                        print(f"Skipped existing student with ID {row['student_id']}")
                except Exception as e:
                    print(f"Error inserting data for {row['student_firstname']} {row['student_lastname']}: {e}")
                # except Exception as e:
                #     # If there's an error during the creation, log the error and continue
                #     print(f"Error inserting data for {row['student_firstname']} {row['student_lastname']}: {e}")
                #     continue  # Optionally, you can decide to fail the whole process or just skip this record

            # Clear the data from the session after successful insertion
            del request.session['excel_data']

            return HttpResponse('Data inserted successfully')
        else:
            return HttpResponse('No data found to insert', status=404)
    else:
        return HttpResponse('POST request expected', status=400)


@login_required
def update_userprofile_views(request):
    # Get the UserProfile instance linked to the current logged-in user.
    # Assuming UserProfile has a one-to-one link to the User model.
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Pass the instance of the existing profile to the form.
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            # Redirect to a success page or profile detail view.
            return redirect('update_userprofile')
    else:
        # If not a POST request, instantiate the form with the existing profile data.
        form = UserProfileForm(instance=user_profile)

    return render(request, 'UpdateInstanceForm.html', {'form': form})


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Class_Enrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer

class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Student_Enrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
