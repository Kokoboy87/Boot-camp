from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context ={
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else :
        course = Course.objects.create(
            name=request.POST['name']
        )
        desc = Description.objects.create(content=request.POST['desc'])
        course.description = desc
        course.save()
        
    return redirect('/')

def delete(request, course_id):
    if request.method == 'GET':
        context ={
            'course': Course.objects.get(id=course_id)
        }
        return render(request, 'delete.html', context)
    if request.method=='POST':
        course = Course.objects.get(id=course_id)
        course.delete()
        return redirect('/')
