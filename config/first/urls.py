from .views import home, student, course,  first_page
from django.urls import path

urlpatterns = [
    path('', home),
    path('first_page/', first_page),
    path('students/', student),
    path('courses/', course),
]
