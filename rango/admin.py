from django.contrib import admin
from rango.models import Category, Page, UserProfile

"""
class PageInline(admin.TabularInline):
    model = Page
    extra = 1
"""

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'views', 'likes')
    list_filter = ['name']
    search_fields = ['name']
    #inlines = [PageInline]

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)
