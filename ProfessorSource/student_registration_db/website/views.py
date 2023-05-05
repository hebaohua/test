from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student, Product

def welcome(request):
    # return HttpResponse("Welcome to Django - the great MVC Framework !!!")
    return render(request, "website/welcome.html",
                  {"message":"Raj Joseph","ag":"25","fontsizes":[1,2,3,4,5,6,7,8,9],
                   "number_of_students":Student.objects.count(),
                   "students":Student.objects.all()})

def index(request):
    return render(request, "website/index.html",{"products":Product.objects.all()})