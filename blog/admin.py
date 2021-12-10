from django.contrib import admin
from .models import Authors, Category, Book, URL, News


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(URL)
admin.site.register(News)
admin.site.register(Authors)



