from django.contrib import admin
import admin_thumbnails
from .models import Product, Color, Images, Variants, Review, Connection



@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
	model = Images
	readonly_fields = ('id',)
	extra = 1


class ProductVariantsInline(admin.TabularInline):
	model = Variants
	readonly_fields = ('image_variants',)
	extra = 1
	show_change_link = True

# class ProductImagesInline(admin.TabularInline):
# 	model = ProductImages
# 	readonly_fields = ('id',)
# 	extra = 1

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
	list_display = ['id','image','title','image_thumbnail','slug']
	prepopulated_fields = {'slug': ('title',)}

@admin_thumbnails.thumbnail('image')
class ProductAdmin(admin.ModelAdmin):
	list_display = ['id','name','price','image_is']
	list_filter = ['name']
	readonly_fields = ('image_is',)
	inlines = [ProductImageInline,ProductVariantsInline]

class ColorAdmin(admin.ModelAdmin):
	list_display =['name', 'code', 'color_tag', 'get_color']



class ProductImageAdmin(admin.ModelAdmin):
	list_display = ['title',]
	# inlines =[ProductImageInline]	

      
	
# class SizeAdmin(admin.ModelAdmin):
# 	list_display = ['name','code']
	
class VariantsAdmin(admin.ModelAdmin):
	list_display = ['title','product','color','quantity','image','image_variants']


@admin_thumbnails.thumbnail('image')	
class ReviewAdmin(admin.ModelAdmin):
	list_display = ['stars','image']
	
admin.site.register(Color,ColorAdmin)
# admin.site.register(Size,SizeAdmin)
admin.site.register(Variants,VariantsAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Connection)


# admin.site.register(ProductImages,ProductImageAdmin)