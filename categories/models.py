from django.db import models

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title
   

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    subcategory = models.ManyToManyField(Subcategory, blank=True, related_name='sb')
    image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.title