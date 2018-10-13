from django.conf.urls import url
from . import views
from django.urls import include, path

app_name = 'charts'
urlpatterns = [
    path('', views.charts, name='charts')
]
