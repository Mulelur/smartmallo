from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField

class SubCategory(models.Model):
    title = models.CharField(max_length=90)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title  


class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)
    # subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title



class CSA(models.Model):
    title = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title

    


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory_slug = models.SlugField(blank=True)
    csa = models.ForeignKey(CSA, on_delete=models.CASCADE)
    text = RichTextUploadingField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title








