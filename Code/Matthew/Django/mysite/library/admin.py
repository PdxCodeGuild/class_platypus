from django.contrib import admin

from .models import Book, Author, BookCheckout


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookCheckout)
