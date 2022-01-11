from django.contrib import admin

from .models import Category, Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'created')
    list_filter = ('published',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
