from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('rps/', include('rps.urls')),
    path('contacts/', include('contacts.urls')),
    path('todo/', include('todo.urls')),
    path('todoajax/', include('todoajax.urls')),
]