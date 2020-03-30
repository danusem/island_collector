from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('islands/', views.islands_index, name='index'),
    path('islands/<int:island_id>/', views.islands_detail, name='detail'),
    path('islands/create/', views.IslandCreate.as_view(), name='islands_create'),
    path('islands/<int:pk>/update/', views.IslandUpdate.as_view(), name='islands_update'),
    path('islands/<int:pk>/delete/', views.IslandDelete.as_view(), name='islands_delete'),
]