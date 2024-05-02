from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Course(models.Model):
    course_id = models.AutoField(primary_key=True, verbose_name=" Course ID")
    course_code = models.CharField(max_length=255, verbose_name="Code")
    course_name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.course_name


class Student(models.Model):
    student_id = models.AutoField(primary_key=True, verbose_name="Student ID")
    student_firstname = models.CharField(max_length=255, verbose_name="First Name")
    student_lastname = models.CharField(max_length=255, verbose_name="Last Name")
    student_email = models.EmailField(verbose_name="Email")
    student_DOB = models.DateField(verbose_name="Date of Birth")

    def __str__(self):
        return f'{self.student_firstname} {self.student_lastname}'


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True, verbose_name="Semester ID")

    semester_year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
        verbose_name="Year"
    )
    semester_name = models.CharField(max_length=255, verbose_name="Semester")
    def __str__(self):
        return self.semester_name


class Lecturer(models.Model):
    staff_id = models.AutoField(primary_key=True, verbose_name="Staff ID")
    lecturer_firstname = models.CharField(max_length=255, verbose_name="First Name")
    lecturer_lastname = models.CharField(max_length=255, verbose_name="Last Name")
    lecturer_email = models.EmailField(verbose_name="Email")
    lecturer_DOB = models.DateField(verbose_name="Date of Birth")

    def __str__(self):
        return f'{self.lecturer_firstname}_{self.lecturer_lastname}'


class Class_Enrollment(models.Model):  # Class
    class_id = models.AutoField(primary_key=True, verbose_name="ID")
    class_number = models.IntegerField(verbose_name="Number")
    class_semester = models.ForeignKey('Semester', on_delete=models.CASCADE, verbose_name="Semester")
    class_course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="Course")
    class_lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE, verbose_name="Lecturer")

    def __str__(self):
        return str(self.class_id)


class Student_Enrollment(models.Model):
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name="Student ID")
    class_id = models.ForeignKey('Class_Enrollment', on_delete=models.CASCADE, verbose_name="Class ID")
    grade_year = models.IntegerField(verbose_name="Grade")
    enrollment_date = models.DateField(verbose_name="Enrollment DateTime")
    grade_date = models.DateField(verbose_name="Grade DateTime")

    class Meta:
        unique_together = ('student_id', 'class_id')  # enforce composite primary key

    def __str__(self):
        return f'name:{self.student_id}&class{self.class_id}'
