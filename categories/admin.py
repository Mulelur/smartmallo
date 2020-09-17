from django.contrib import admin
from .models import Category, Subcategory
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['title','slug','image']
    prepopulated_fields = {'slug': ('title',)}

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}    


admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Category, CategorieAdmin)