from django.contrib import admin
from .models import Post, Chapter, ChapterImage, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

class ChapterImageInline(admin.TabularInline):
    model = ChapterImage
    extra = 3

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'user')
    search_fields = ('title', 'body')
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    inlines = [ ChapterImageInline, ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'user')
    search_fields = ('title', 'body')
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


