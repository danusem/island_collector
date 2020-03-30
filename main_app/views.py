from django.shortcuts import render
from django.views.generic.edit import CreateView

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
    island = Island.objects.get(id=island_id)
    return render(request, 'islands/detail.html', {'island': island })

class IslandCreate(CreateView):
    model = Island
    fields = '__all__'