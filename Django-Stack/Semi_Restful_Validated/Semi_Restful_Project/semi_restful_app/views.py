from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def home(request):
    context ={
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        Show.objects.create(
            title = request.POST['title'],
            networks = request.POST['networks'],
            release_date = request.POST['release_date'],
            description = request.POST['description'],
    )
    return redirect('/')

def edit(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context ={
        'show': one_show 
    }
    return render(request, 'edit.html', context)

def show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context ={
        'show': one_show 
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/')

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/{show_id}/edit')
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.networks = request.POST['networks']
        show.description = request.POST['description']
        show.release_date = request.POST['release_date']
        show.save()
        print(show)
        messages.success(request, "Show successfully updated")
        return redirect('/')