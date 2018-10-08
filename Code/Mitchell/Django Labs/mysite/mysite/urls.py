from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('todo/', include('todo.urls')),
    path('urlshort/', include('urlshort.urls')),
    path('admin/', admin.site.urls),
]
