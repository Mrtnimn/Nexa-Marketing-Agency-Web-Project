from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Website/index.html')

def portfolioDetails(request):
    return render(request, 'Website/portfolio-details.html')

def serviceDetails(request):
    return render(request, 'Website/service-details.html')