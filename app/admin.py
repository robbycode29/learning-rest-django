# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app.models import Publisher, Author, Book

from django.contrib import admin

# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    list_filter = ('city', 'state_province', 'country')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('salutation', 'first_name', 'last_name', 'email')
    list_filter = ('salutation',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')    
    list_filter = ('publication_date',)
    ordering = ('-publication_date',)
    search_fields = ('title',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
