from django.contrib import admin
from django.urls import path
from API_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api)
]
