from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'socoolMediaManager'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('addPlatform/', views.addPlatform, name='addPlatform'),
    path('deletePlatform/', views.deletePlatform, name='deletePlatform'),
    path('register/', views.register, name='register'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
]