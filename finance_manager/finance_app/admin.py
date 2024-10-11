from django.contrib import admin
from .models import TodoItem, AppItem

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(AppItem)