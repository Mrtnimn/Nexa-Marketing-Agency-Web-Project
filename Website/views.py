from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def portfolioDetails(request):
    return render(request, 'portfolio-details.html')

def serviceDetails(request):
    return render(request, 'service-details.html')