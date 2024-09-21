from django.shortcuts import render

# Create your views here.
def css (request):
    return render(request,css.html)