from django.urls import  path

from . import views

app_name = 'my_example'
urlpatterns = [
    path('', views.index, name='index'),
	path('json/', views.json_post, name='json_post'),
]
