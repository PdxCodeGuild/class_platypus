from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('addItem/', views.addItem, name='addItem'),
    path('deleteItem/', views.deleteItem, name='deleteItem'),
    path('completeItem/', views.completeItem, name='completeItem')

]
