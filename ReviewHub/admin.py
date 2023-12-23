# Register your models here.
from django.contrib import admin

from ReviewHub.models import Book, Review

admin.site.register(Book)
admin.site.register(Review)
