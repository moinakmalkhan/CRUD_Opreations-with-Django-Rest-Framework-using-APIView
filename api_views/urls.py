
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentapifunctionbased/", views.FunctionBasedStudentAPI),
    path("studentapifunctionbased/<int:pk>", views.FunctionBasedStudentAPI),
    path("studentapiclassbased/", views.ClassBasedStudentAPI.as_view()),
    path("studentapiclassbased/<int:pk>", views.ClassBasedStudentAPI.as_view()),
]
