from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gradebook.models import Class_Enrollment, Course, Lecturer, Semester, Student, Student_Enrollment, UserProfile


class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if the email is already registered with a User
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        # Check if the email exists in either Students or Lecturers
        student_exists = Student.objects.filter(student_email=email).exists()
        lecturer_exists = Lecturer.objects.filter(lecturer_email=email).exists()
        if not (student_exists or lecturer_exists):
            raise forms.ValidationError("This email is not authorized to register.")
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


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
