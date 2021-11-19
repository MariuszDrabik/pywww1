from django.contrib import admin

from .models import Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'created')
    list_filter = ('published',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
