from django.db import models



from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    slug = models.CharField(max_length=50,null=False,blank=False)
    name = models.CharField(max_length=50,null=False,blank=False)
    image = models.ImageField(upload_to="imagesS",null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self) :
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=100,null=False,blank=False)
    name = models.CharField(max_length=100,null=False,blank=False) 
    product_image = models.ImageField(upload_to="imagess",null=False,blank=False)
    description = models.CharField(max_length=500,null=False,blank=False)
    quntity = models.IntegerField(null=False,blank=False)
    orginal_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default,1=Hidden")  
    trending = models.BooleanField(default=False,help_text="0=default,1=Hidden")
    
    
    def __str__(self):
        return self.name 
    

class Coustmer(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=50)
    address=models.TextField()





#for api

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.key






