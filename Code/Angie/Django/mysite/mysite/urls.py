from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('urlshort/', include('urlshort.urls')),
    path('polls/', include('polls.urls')),
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]