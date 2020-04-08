from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Island, Characteristic, Photo
from .forms import WeatherForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid 
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'islandcollector'

# Create your views here.
def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Sign Up - Try Again'

    form = UserCreationForm()
    context = {'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def islands_index(request):
    islands = Island.objects.filter(user=request.user)
    return render(request, 'islands/index.html', {'islands': islands })

@login_required
def islands_detail(request, island_id):

    island = Island.objects.get(id=island_id)
    weather_form = WeatherForm()

    characteristics_island_doesnt_have = Characteristic.objects.exclude(id__in=island.characteristics.all().values_list('id'))

    return render(request, 'islands/detail.html',
        {
            'island': island,
            'weather_form': weather_form,
            'characteristics': characteristics_island_doesnt_have
        }
    )

@login_required
def add_forecast(request, island_id):
    
    form = WeatherForm(request.POST)

    if form.is_valid():
        new_forecast = form.save(commit=False)
        new_forecast.island_id = island_id
        new_forecast.save()

    return redirect('detail', island_id=island_id)

@login_required
def assoc_characteristic(request, island_id, characteristic_id):
    Island.objects.get(id=island_id).characteristics.add(characteristic_id)
    return redirect('detail', island_id=island_id)

@login_required
def add_photo(request, island_id):
    photo_file = request.FILES.get('photo-file', None)

    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, island_id=island_id)
            photo.save()
        except:
            print('An error has occurred uploading file to s3')
    return redirect('detail', island_id=island_id)

class IslandCreate(LoginRequiredMixin, CreateView):
    model = Island
    fields = ['name', 'country', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IslandUpdate(LoginRequiredMixin, UpdateView):
    model = Island
    fields = ['country', 'description']

class IslandDelete(LoginRequiredMixin, DeleteView):
    model = Island
    success_url = '/islands/'

class CharacteristicList(LoginRequiredMixin, ListView):
    model = Characteristic

class CharacteristicDetail(LoginRequiredMixin, DetailView):
    model = Characteristic

class CharacteristicCreate(LoginRequiredMixin, CreateView):
    model = Characteristic
    fields = ['name']
    success_url = '/characteristics/'

class CharacteristicUpdate(LoginRequiredMixin, UpdateView):
    model = Characteristic
    fields = ['name']
    success_url = '/characteristics/'

class CharacteristicDelete(LoginRequiredMixin, DeleteView):
    model = Characteristic
    success_url = '/characteristics/'