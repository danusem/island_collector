from django.forms import ModelForm
from .models import Weather

class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = ['date', 'forecast']
