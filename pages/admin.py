from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'status',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('title', 'status',)
    prepopulated_fields = {'slug': ('title',)}
