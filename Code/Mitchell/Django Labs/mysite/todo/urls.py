from django.urls import path
from . import views

app_name = '<app name>'
urlpatterns = [
    path('<path>', views.index, name='index')
]
