from django.shortcuts import render

# Create your views here.
def dummy(request):
    return render(request,'dummy.html')
def home(request):
    return render(request,'home.html')
def buttons(request):
    return render(request,'buttons.html')
def corousel(request):
    return render(request,'corousel.html')
def cards(request):
    return render(request,'cards.html')
def toasts(request):
    return render(request,'toasts.html')
def alerts(request):
    return render(request,'alerts.html')