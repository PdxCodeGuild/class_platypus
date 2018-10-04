from django.urls import path

from . import views


urlpatterns = [

    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),
]
