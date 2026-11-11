from django.contrib import admin
from .models import ToDoItem


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ("text", "due_date")
    list_filter = ("due_date",)
    search_fields = ("text",)
