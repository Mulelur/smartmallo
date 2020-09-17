from django.contrib import admin
from .models import Article, SubCategory, Category, CSA

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    prepopulated_fields = {'slug': ('title',)}

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','id']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article,ArticleAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CSA)

