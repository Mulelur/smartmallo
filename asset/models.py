from django.db import models
from django.utils.safestring import mark_safe


class Benar(models.Model):
    page_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='benars')

    def __(self):
        return self.page_name


    def image_is(self):
        img2 = Benar.objects.get(image=self.image)
        if img2.id is not None:
                return mark_safe('<img src="{}" />'.format(img2.image.url))  
        else:     
            return ""   

    def get_banner(self):
        img = Benar.objects.get(image=self.image)
        if img.id is not None:
                return mark_safe('< data-image-src="{}" />'.format(img.image.url))  
        else:     
            return ""   
            
