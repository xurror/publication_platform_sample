from django.contrib import admin
from .models import NewsDetails
# Register your models here.
class NewsDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'editor', 'published_date')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('editor', 'title',)
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(NewsDetails, NewsDetailsAdmin)