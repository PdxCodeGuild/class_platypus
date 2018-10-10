from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'socoolMediaManager'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('addPlatform/', views.addPlatform, name='addPlatform'),
    path('deletePlatform/', views.deletePlatform, name='deletePlatform'),
]