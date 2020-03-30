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

def islands_detail(request, island_id):
    island = Island.object.get(id=island_id)
    return render(request, 'islands/detail.html', {'island': island })