from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
    else:                               # this method make the reset start from 0
        request.session["count"] += 1
    request.session["word"] = get_random_string(length=14)
    # request.session["count"] += 1    # and this method make the reset start from 1
    return render(request, 'index.html' )

def reset(request):
    request.session.clear()
    return redirect('/random_word')