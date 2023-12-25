from django.contrib import admin
from modelrelationshipapp.models import Book, Post, Dance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'book_author', 'book_publish_date', 'user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_category', 'post_publish_date', 'user']


@admin.register(Dance)
class DanceAdmin(admin.ModelAdmin):
    list_display = ['dance_name', 'dance_duration', 'dance_by']
