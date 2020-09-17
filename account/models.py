from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)



    def __str__(self):
        return f'{self.user.username} Profile'

class TrackOrder(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
    Order_number = models.CharField(max_length=13)

    def __str__(self):
        return self.user

class Shipping(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name        


