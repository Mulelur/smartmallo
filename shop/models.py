from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date
from categories.models import Category, Subcategory



from ckeditor_uploader.fields import RichTextUploadingField
    


class Color(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True, null=True)  

    def __str__(self):
        return self.name

    def get_color(self):
        return format_html('<p style="background: {}; color: white;">color</p>'.format(self.code))      
    
    def get_wishlist(self):
        return mark_safe('<img style="display: inline-block;margin-top: 10px;" height="16" width="17" src="{% static "png/heart.png" %}" >')
    
    def color_tag(self):
        if self.code is None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""

    def __str__(self):
        return self.name

class Product(models.Model):
    VARIANTS = (
        ('None','None'),
        ('Size','Size'),
        ('Color','Color'),
        ('Color & Size','Color & Size')
    )
    STATUS = (
        ('Featured','Featured'),
        ('On_Sale','On Sale'),
        ('Best_Rated','Best Rated'),
        ('Best_Seller','Best Seller'),
        ('DOF','Deals Of The week'),
        ('Out_of_Stock','Out of Stock'),
        ('In_Stock','In Stock')
    )
    AVAILABLITY = (
        ('In Stock','In Stock'),
        ('Available', 'Available'),
        ('Shipped In 4-8 days','Shipped In 4-8 days'),
        ('Shipped In 14-28 days', 'Shipped In 14-28 days')
    )
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='product_image', max_length=400)
    price = models.IntegerField()
    discription = RichTextUploadingField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    variant = models.CharField(max_length=10,choices=VARIANTS, default='None', blank=True)
    availablity = models.CharField(max_length=100, choices=AVAILABLITY, default='IS')
    comper_to = models.IntegerField(default=0, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    user_wishlist = models.ManyToManyField(User, blank=True, default=None, related_name='my_new_wishlist')
    quantity = models.IntegerField(default=0)
    # compliment_to = models.ForeignKey(Connection, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=STATUS, default='In_Stock', blank=True)
    descount = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)], default='10', blank=True)

    def get_absolute_url(self):
        return reverse("shop-detail" , args=[self.pk])

    def __str__(self):
        return self.name

    def num_wishlist(self):
        return self.wislist.all().count()    

    # def image_tag(self):
    #     img = Images.objects.get(id=self.id)
    #     if img.id is not None:
    #             return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))  
    #     else:     
    #         return "" 
              
    def image_is(self):
        img2 = Product.objects.get(image=self.image)
        if img2.id is not None:
                return mark_safe('<img src="{}" height="50"/>'.format(img2.image.url))  
        else:     
            return ""

    def no_of_ratings(self):
        ratings = Rating.objects.filter(product=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:        
            return 0



class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to=('images'),  max_length=400)
    slug = models.SlugField(default='', blank=True)
    # image_id = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class Variants(models.Model):
    title = models.CharField(max_length=188, blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0)
    image_variants = models.ImageField(blank=True, upload_to=('image_variants'),  max_length=400)
    comper_to = models.IntegerField(default=0, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    def image(self):
        img = Images.objects.get(id=self.id)
        if img.id is not None:
            varimage=img.image.url
        else:
            varimage=""  
        return varimage   

    def image_tag(self):
        img = Images.objects.get(id=self.id)
        if img.id is not None:
                return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))  
        else:     
            return ""
        # def color_tag(self):
        # if self.code is None:
        #     return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        # else:
        #     return ""        

# class ProductImages(models.Model):

#     title = models.CharField(max_length=100)
#     product_images = models.ImageField(upload_to='product_image', default='')
      

    # def __str__(self):
    #     return self.title
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    review = models.TextField(blank=True)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], blank=True)
    date = models.DateField(default=timezone.now, blank=True)
    image = models.ImageField(upload_to='product_review', blank=True, max_length=1000)

    class Meta:
        unique_together = (('user', 'product'),)
        index_together = (('user', 'product'),)



class Connection(models.Model):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='connect')


    def __str__(self):
        return self.title