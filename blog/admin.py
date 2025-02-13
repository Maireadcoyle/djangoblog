from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin # defines the text editor

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin): # give your admin panel greater functionality and clarity.

    list_display = ('title', 'slug', 'status',)
    search_fields = ['title', 'content',]
    list_filter = ('status', 'is_draft', 'is_featured', 'creation_date')  #dont think i need status, is_featured/is draft
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)