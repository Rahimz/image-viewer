from django.contrib import admin

from .models import Image, Category


# admin.site.register(Image)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']    



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'upload', 'active']
    search_fields = ['name', 'description']
    list_editable = ['name', 'active']
    list_filter = ['active']
