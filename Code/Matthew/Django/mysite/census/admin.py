from django.contrib import admin

from .models import State, County, CensusDatum




admin.site.register(State)
admin.site.register(County)
admin.site.register(CensusDatum)