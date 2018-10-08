from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'todo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('all/', views.all, name='all')
]
