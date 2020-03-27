from django.shortcuts import render
from django.http import HttpResponse

class Island:
    def __init__(self, name, country, description):
        self.name = name
        self.country = country
        self.description = description

islands = [
    Island('Whitsundays', 'Australia', 'Stunning'),
    Island('Bali', 'Indonesia', 'Exotic'),
    Island('Kauai', 'USA', 'Rugged Cliffs'),
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Its an Island Ting</h1>')

def about(request):
    return render(request, 'about.html')

def islands_index(request):
    return render(request, 'islands/index.html', {'islands': islands })