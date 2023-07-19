from django.contrib import admin
from .models import Documentary

@admin.register(Documentary)
class DocumentaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'author')
    search_fields = ('title', 'author')
    list_filter = ('year',)
