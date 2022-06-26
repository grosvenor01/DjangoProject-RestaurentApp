from pickle import FALSE
from secrets import choice
from django.db import models

# Create your models here.
cate=( ('Meal','Meal'),('Fast Food','Fast Food') ,('Drink','Drink'),('Other','Other'))
class food(models.Model):
    name=models.CharField(max_length=100,blank=FALSE)
    food_pic=models.ImageField(upload_to='photos',null=False)
    category=models.CharField(max_length=50,blank=False,choices=cate)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    description=models.TextField()
    def __str__(self):
        return self.name
class order(models.Model):
    quantity=models.IntegerField(blank=False)
    user_name=models.CharField(max_length=100,blank=FALSE)
    email=models.EmailField(max_length=254)
    adress=models.CharField(max_length=200)
    phone=models.DecimalField(max_digits=10,decimal_places=0)
    def __str__(self):
        return self.user_name
    

    
    
    
    