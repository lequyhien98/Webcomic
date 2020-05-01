from django.contrib import admin
from .models import Post, Chap, ChapImage, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class ChapImageInline(admin.TabularInline):
    model = ChapImage
    extra = 3

@admin.register(Chap)
class ChapAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'user')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'body')
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    inlines = [ ChapImageInline, ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'user')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'body')
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


