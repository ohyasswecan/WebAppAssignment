from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gradebook.models import Class_Enrollment, Course,Lecturer,Semester,Student,Student_Enrollment

class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()

class Class_EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Class_Enrollment
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'

class StudentEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Student_Enrollment
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']