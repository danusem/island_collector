from django.shortcuts import render
from .models import Island

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def islands_index(request):
    islands = Island.objects.all()
    return render(request, 'islands/index.html', {'islands': islands })