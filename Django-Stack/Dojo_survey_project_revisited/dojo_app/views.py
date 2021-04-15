from django.shortcuts import render, redirect

def home(request):
    return render(request, "form.html")

def submit_form(request):
    if request.method == 'POST':
            request.session['name'] = request.POST['name']
            request.session['location'] = request.POST['location']
            request.session['language'] = request.POST['language']
            request.session['gender'] = request.POST['gender']
            request.session['comment'] = request.POST['comment']
            return redirect('/result')
    else :
        return render(request, "form.html")

def result(request):
    return render(request, "results.html")

