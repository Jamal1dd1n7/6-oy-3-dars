from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from .models import Course, Student

def home(request: WSGIRequest):
    return render(request, 'intex.html')

def first_page(request: WSGIRequest):
    return render(request, 'first_page.html')
    
def student(request: WSGIRequest):
    students = Student.objects.all()
    print(students)
    # return HttpResponse("Salom")
    return render(request, 'students.html', {'students': students})

def course(request: WSGIRequest):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})