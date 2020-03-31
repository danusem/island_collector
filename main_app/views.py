from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Island
from .forms import WeatherForm

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
    weather_form = WeatherForm()

    return render(request, 'islands/detail.html',
        {
            'island': island,
            'weather_form': weather_form
        }
    )

class IslandCreate(CreateView):
    model = Island
    fields = '__all__'

class IslandUpdate(UpdateView):
    model = Island
    fields = ['country', 'description']

class IslandDelete(DeleteView):
    model = Island
    success_url = '/islands/'