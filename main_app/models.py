from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

FORECAST = (
    ('S', 'Sunny'),
    ('C', 'Cloudy'),
    ('R', 'Rainy')
)

# Create your models here.

class Characteristic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Island(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    characteristics = models.ManyToManyField(Characteristic)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'island_id': self.id })

class Weather(models.Model):
    date = models.DateField()
    forecast = models.CharField(
        max_length=1,
        choices=FORECAST,
        default=FORECAST[0][0]
    )

    island = models.ForeignKey(Island, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_forecast_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    island = models.ForeignKey(Island, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for island_id: {self.island_id} @{self.url}"