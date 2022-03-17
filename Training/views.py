from django.shortcuts import render

# Create your views here.



#***********************developer**************************************************
def course(request):
    return render(request,'course\course.html')
def course_add(request):
    return render(request,'course\course_add.html')
def course_addnew(request):
    return render(request,'course\course_addnew.html')
def course_category(request):
    return render(request,'course\course_category.html')
def course_courses(request):
    return render(request,'course\course_courses.html')
def course_course_details(request):
    return render(request,'course\course_course_details.html')