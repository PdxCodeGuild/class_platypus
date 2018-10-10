from django.contrib import admin

from django.contrib import admin

from .models import Books, Circulation, Author

admin.site.register(Books)
admin.site.register(Circulation)
admin.site.register(Author)