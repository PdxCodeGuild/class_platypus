from django.urls import  path

from . import views

app_name = 'my_example'
urlpatterns = [
    path('', views.index, name='index'),
    path('json/', views.json_get, name='json_get'),
]
