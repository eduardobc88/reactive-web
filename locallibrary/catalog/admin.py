from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.


# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'display_language') # archive page
    fields = ['title', 'author', 'summary', 'genre', ('isbn', 'language', 'slug')] # single page
    readonly_fields = ['slug']
    pass


# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'slug']
    print('== admin ==', Author.slug)
    readonly_fields = ['slug']
    pass


admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)