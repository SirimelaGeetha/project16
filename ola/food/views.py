from django.shortcuts import render

# Create your views here.

def chocolate(request):
    return render(request, 'chocolate.html')
