from django.contrib import admin
from .models import Author, Book
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from import_export import resources


class BookResource(resources.ModelResource):
    
    class Meta:
        model = Book
        # fields = ('id', 'title', 'description')


class BookAdmin(ImportExportModelAdmin):
    list_display = ('title', 'slug', 'published', 'available')
    list_filter = ('published', 'available')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    resource_class = BookResource


        


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
