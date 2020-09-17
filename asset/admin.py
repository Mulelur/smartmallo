from django.contrib import admin
from .models import Benar
import admin_thumbnails


class BenarAdmin(admin.ModelAdmin):
    list_display = ['id','page_name','image_is']
    readonly_fields = ('image_is',)

admin.site.register(Benar,BenarAdmin)    

