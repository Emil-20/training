"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Training import views

urlpatterns = [
    




    #***********************course***********************************************

    path('course/',views.course, name='course'),
    path('course_add/',views.course_add, name='course_add'),
    path('course_addnew/',views.course_addnew, name='course_addnew'),
    path('course_category/',views.course_category, name='course_category'),
    path('course_courses/',views.course_courses, name='course_courses'),
    path('course_course_details/',views.course_course_details, name='course_course_details'),
    
]
