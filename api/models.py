from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        return self.title

class Collection(models.Model):
    collection = models.CharField(max_length=100)
    
    def __str__(self):
        return self.collection
    
class Vendor(models.Model):
    vendor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.vendor
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    compare_at_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    margin = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    collection = models.CharField(max_length=255, null=True, blank=True)
    stock = models.IntegerField(null=True)
    vendor = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    status = models.CharField(max_length=25, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=1000, blank=True)
    variant = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return self.name
    
class Blog(models.Model):
    blog = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog
    
class Blogpost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogauthor")
    tags = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    blog = models.CharField(null=True, blank=True, max_length=150)
    # blog = models.ForeignKey(Blog, null=True, blank=True, on_delete=models.CASCADE, related_name="blogpost")
    
    def __str__(self):
        return self.title