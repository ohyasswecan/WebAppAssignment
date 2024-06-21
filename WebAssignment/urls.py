"""
URL configuration for WebAssignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from WebAssignment import settings
from gradebook.views import (
    IndexView, RegisterView,
    CourseViewSet, SemesterViewSet, LecturerViewSet, StudentViewSet, ClassEnrollmentViewSet, StudentEnrollmentViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'semesters', SemesterViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'students', StudentViewSet)
router.register(r'class_enrollments', ClassEnrollmentViewSet)
router.register(r'student_enrollments', StudentEnrollmentViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # React index view
    path('account/login/', LoginView.as_view(template_name='registration/Login.html'), name='login'),
    path('account/logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to home page after logout
    path('account/register/', RegisterView.as_view(), name='register'),
    path('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('app/',include('gradebook.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
