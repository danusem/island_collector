from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('islands/', views.islands_index, name='index'),
    path('islands/<int:island_id>/', views.islands_detail, name='detail'),
]