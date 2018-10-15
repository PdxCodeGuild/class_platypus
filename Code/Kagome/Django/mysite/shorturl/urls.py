from django.urls import path

from . import views

app_name = 'shorturl'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('r/<str:code>/', views.redirect, name='redirect')
]
