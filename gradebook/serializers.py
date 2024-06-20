from rest_framework import serializers
from .models import Course, Semester, Lecturer, Student, Class_Enrollment, Student_Enrollment


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClassEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Enrollment
        fields = '__all__'

class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Enrollment
        fields = '__all__'
