from django.shortcuts import render
from time import localtime, strftime

def time_page(request):
    context = {
        "time": strftime("%b-%d-%Y %I:%M %p", localtime())
    }
    return render(request, 'time.html', context)

# Create your views here.
