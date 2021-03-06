# Generated by Django 2.2 on 2020-07-04 12:47

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(max_length=400, upload_to='product_image')),
                ('price', models.IntegerField()),
                ('discription', ckeditor_uploader.fields.RichTextUploadingField()),
                ('variant', models.CharField(blank=True, choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Color & Size', 'Color & Size')], default='None', max_length=10)),
                ('availablity', models.CharField(choices=[('In Stock', 'In Stock'), ('Available', 'Available'), ('Shipped In 4-8 days', 'Shipped In 4-8 days'), ('Shipped In 14-28 days', 'Shipped In 14-28 days')], default='IS', max_length=100)),
                ('comper_to', models.IntegerField(blank=True, default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(blank=True, choices=[('Featured', 'Featured'), ('On_Sale', 'On Sale'), ('Best_Rated', 'Best Rated'), ('Best_Seller', 'Best Seller'), ('DOF', 'Deals Of The week'), ('Out_of_Stock', 'Out of Stock'), ('In_Stock', 'In Stock')], default='In_Stock', max_length=100)),
                ('descount', models.IntegerField(blank=True, default='10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Color')),
                ('user_wishlist', models.ManyToManyField(blank=True, default=None, related_name='my_new_wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=188, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0)),
                ('image_variants', models.ImageField(blank=True, max_length=400, upload_to='image_variants')),
                ('comper_to', models.IntegerField(blank=True, default=0)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, max_length=400, upload_to='images')),
                ('slug', models.SlugField(blank=True, default='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('products', models.ManyToManyField(related_name='connect', to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True)),
                ('stars', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, max_length=1000, upload_to='product_review')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
                'index_together': {('user', 'product')},
            },
        ),
    ]
