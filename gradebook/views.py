from django.contrib.auth import login
from rest_framework import generics, status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Class_Enrollment, Course, Semester, Student, Lecturer, Student_Enrollment, UserProfile
from .forms import Class_EnrollmentForm, CourseForm, SemesterForm, StudentForm, LecturerForm, StudentEnrollmentForm, \
    UploadExcelForm, UserProfileForm, CustomUserCreationForm
from .serializers import CourseSerializer, SemesterSerializer, LecturerSerializer, StudentSerializer, \
    ClassEnrollmentSerializer, StudentEnrollmentSerializer
import pandas as pd
import datetime


class MyTokenObtainPairView(TokenObtainPairView):
    pass


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_profile = user.profile  # Assuming OneToOne relationship is set
        return Response({
            'username': user.username,
            'email': user.email,
            'role': user_profile.role,
            'avatar': user_profile.avatar.url if user_profile.avatar else None
        })


# Base Reflex View
class BaseReflexView(APIView):
    def get(self, request):
        return render(request, 'base.html')


# Index View
class IndexView(APIView):
    def get(self, request):
        return render(request, 'index.html')


# Home View
class HomeView(APIView):
    def get(self, request):
        return render(request, 'home.html')


# Class Enrollment Views
class ClassEnrollmentListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Class_Enrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer
    permission_classes = [AllowAny]
    ordering = ['class_id']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Class_EnrollmentForm()
        context['user'] = self.request.user
        return context


class ClassEnrollmentDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Class_Enrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer
    permission_classes = [AllowAny]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Course Views
class CourseListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    ordering = ['course_id']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CourseForm()
        context['user'] = self.request.user
        return context


class CourseDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Semester Views
class SemesterListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]
    ordering = ['semester_id']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SemesterForm()
        context['user'] = self.request.user
        return context


class SemesterDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Student Views
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StudentListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        context['user'] = self.request.user
        return context


class StudentDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Lecturer Views
class LecturerListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]
    ordering = ['staff_id']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LecturerForm()
        context['user'] = self.request.user
        return context


class LecturerDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


# Enrollment Views
class EnrollmentListView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Student_Enrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [AllowAny]
    ordering = ['-enrollment_date']
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentEnrollmentForm()
        context['user'] = self.request.user
        return context


class EnrollmentDetailView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_Enrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [AllowAny]


# Class Create/Update/Delete Views
class CreateClassView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Class_Enrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class UpdateClassView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = Class_Enrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save()


class DeleteClassView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Class_Enrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        instance.delete()


# Course Create/Update/Delete Views
class CreateCourseView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class UpdateCourseView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save()


class DeleteCourseView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        instance.delete()


# Semester Create/Update/Delete Views
class CreateSemesterView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class UpdateSemesterView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save()


class DeleteSemesterView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        instance.delete()


# Student Create/Update/Delete Views
class CreateStudentView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class UpdateStudentView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save()


class DeleteStudentView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        instance.delete()


# Lecturer Create/Update/Delete Views
class CreateLecturerView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class UpdateLecturerView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save()


class DeleteLecturerView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        instance.delete()


# Student Enrollment Create/Update/Delete Views
class CreateStudentEnrollmentView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Student_Enrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class UpdateStudentEnrollmentView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = Student_Enrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save()


class DeleteStudentEnrollmentView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Student_Enrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.delete()


# User Registration View
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/Register.html', {'form': form})

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/Register.html', {'form': form})


# Upload Excel View
class UploadExcelView(APIView):
    def post(self, request):
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            request.session['excel_data'] = df.to_dict(orient='records')
            df_html = df.to_html(classes='table table-striped')
            return Response({'data': df.to_dict(orient='records')}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid form'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        form = UploadExcelForm()
        return Response({'message': 'GET method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Insert List View
import logging

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class InsertListView(APIView):
    parser_classes = [JSONParser]  # Ensure JSON parser is used

    def post(self, request):
        try:
            df_records = request.data  # Access the request body directly
            logger.debug(f"Received data: {df_records}")

            if df_records:
                for row in df_records:
                    try:
                        logger.debug(f"Processing row: {row}")
                        parsed_date = datetime.datetime.strptime(row['student_DOB'], '%m/%d/%Y')
                        formatted_date = parsed_date.strftime('%Y-%m-%d')
                        obj, created = Student.objects.get_or_create(
                            student_id=row['student_id'],
                            defaults={
                                'student_firstname': row['student_firstname'],
                                'student_lastname': row['student_lastname'],
                                'student_email': row['student_email'],
                                'student_DOB': formatted_date
                            }
                        )
                        if created:
                            logger.debug(f"Created new student: {obj}")
                        else:
                            logger.debug(f"Skipped existing student with ID {row['student_id']}")
                    except Exception as e:
                        logger.error(
                            f"Error inserting data for {row['student_firstname']} {row['student_lastname']}: {e}")

                return JsonResponse({'message': 'Data inserted successfully'}, status=201)
            else:
                logger.debug("No data found to insert")
                return JsonResponse({'message': 'No data found to insert'}, status=404)
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            return JsonResponse({'message': 'Error processing request'}, status=500)

    def get(self, request):
        return JsonResponse({'message': 'POST request expected'}, status=400) \
 \
 \
# Update User Profile View
class UpdateUserProfileView(LoginRequiredMixin, APIView):
    def post(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('update_userprofile')
        return render(request, 'UpdateInstanceForm.html', {'form': form})

    def get(self, request):
        user_profile = get_object_or_404(UserProfile, user=request.user)
        form = UserProfileForm(instance=user_profile)
        return render(request, 'UpdateInstanceForm.html', {'form': form})


# ViewSets
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [AllowAny]


class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [AllowAny]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]


class ClassEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Class_Enrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer
    permission_classes = [AllowAny]


class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Student_Enrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [AllowAny]
