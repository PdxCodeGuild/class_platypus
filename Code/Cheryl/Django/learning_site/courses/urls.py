from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from django.urls import include, path

urlpatterns = [
    path('', views.course_list),
    path('<int:course_pk>/<int:step_pk>', views.step_detail),
    path('<int:pk>/', views.course_detail),
]