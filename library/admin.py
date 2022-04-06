from django.contrib import admin

from library.models import Book, MyUser

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Book)
