from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('amiiboHub/', include('amiiboHub.urls')),
    path('socoolMediaManager/', include('socoolMediaManager.urls')),
    path('admin/', admin.site.urls),
]
