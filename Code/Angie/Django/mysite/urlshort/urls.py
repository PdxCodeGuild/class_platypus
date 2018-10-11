from django.urls import path

from . import views

app_name = 'urlshort'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveUrl/', views.saveUrl, name='saveUrl'),
    path('r/<str:code>', views.redirect, name='redirect')


]
