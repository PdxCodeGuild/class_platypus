from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.urls import include, path

urlpatterns = [
    path('', views.course_list),
    path('<int:pk>/', views.course_detail),
]