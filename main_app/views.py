from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Island, Characteristic
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
            'weather_form': weather_form,
        }
    )

def add_forecast(request, island_id):
    
    form = WeatherForm(request.POST)

    if form.is_valid():
        new_forecast = form.save(commit=False)
        new_forecast.island_id = island_id
        new_forecast.save()

    return redirect('detail', island_id=island_id)

# def assoc_characteristic(request, island_id, characteristic_id):
#     Island.objects.get(id=island_id).characteristics.add(characteristics_id)
#     return redirect('detail', island_id=island_id)

class IslandCreate(CreateView):
    model = Island
    fields = '__all__'

class IslandUpdate(UpdateView):
    model = Island
    fields = ['country', 'description']

class IslandDelete(DeleteView):
    model = Island
    success_url = '/islands/'

class CharacteristicList(ListView):
    model = Characteristic

class CharacteristicDetail(DetailView):
    model = Characteristic

class CharacteristicCreate(CreateView):
    model = Characteristic
    fields = ['name']
    success_url = '/characteristics/'

class CharacteristicUpdate(UpdateView):
    model = Characteristic
    fields = ['name']
    success_url = '/characteristics/'

class CharacteristicDelete(DeleteView):
    model = Characteristic
    success_url = '/characteristics/'