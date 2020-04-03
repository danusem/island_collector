from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('islands/', views.islands_index, name='index'),
    path('islands/<int:island_id>/', views.islands_detail, name='detail'),
    path('islands/<int:island_id>/add_forecast/', views.add_forecast, name='add_forecast'),
    path('islands/create/', views.IslandCreate.as_view(), name='islands_create'),
    path('islands/<int:pk>/update/', views.IslandUpdate.as_view(), name='islands_update'),
    path('islands/<int:pk>/delete/', views.IslandDelete.as_view(), name='islands_delete'),
    path('characteristics/<int:pk>/', views.CharacteristicDetail.as_view(), name='characteristics_detail'),
    path('characteristics/<int:pk>/update/', views.CharacteristicUpdate.as_view(), name='characteristics_update'),
    path('characteristics/<int:pk>/delete/', views.CharacteristicDelete.as_view(), name='characteristics_delete'),
    path('characteristics/create/', views.characteristicCreate.as_view(), name='characteristics_create'),
    # path('cats/<int:cat_id>/assoc_characteristic/<int:characteristic_id>/', views.assoc_characteristic, name='assoc_characteristic'),
]