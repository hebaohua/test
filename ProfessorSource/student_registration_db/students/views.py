from django.shortcuts import render

from .models import Student

def detail(request, id):
    student = Student.objects.get(pk=id)
    return render(request, "students/detail.html", {"student": student})
# Create your views here.
