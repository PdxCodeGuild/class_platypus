from django.conf.urls import url
from . import views
from django.urls import include, path

app_name = 'demograph'
urlpatterns = [
    path('', views.index, name='index'),


]