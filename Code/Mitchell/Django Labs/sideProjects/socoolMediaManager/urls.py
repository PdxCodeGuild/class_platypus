from django.urls import path
from . import views

app_name = 'socoolMediaManager'
urlpatterns = [
    path('', views.index, name='index'),
    path('addPlatform/', views.addPlatform, name='addPlatform'),
    path('clearPlatforms/', views.clearPlatforms, name='clearPlatforms'),
]