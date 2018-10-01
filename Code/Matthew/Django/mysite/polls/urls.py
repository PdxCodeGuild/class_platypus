from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewa/', views.viewa, name='index'),
    path('viewb/', views.viewb, name='index'),
    path('viewc/', views.viewc, name='index'),
]