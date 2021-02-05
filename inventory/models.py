from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    categoryname = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    def __str__(self):
        return self.categoryname

class SubCategory(models.Model):
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategoryname = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    def __str__(self):
        return self.subcategoryname

class Brand(models.Model):
    brandname = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    def __str__(self):
        return self.brandname


class Product(models.Model):
    productname = models.CharField(max_length=150)
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategoryid = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brandid = models.ForeignKey(Brand, on_delete=models.CASCADE)
    modelnumber = models.CharField(max_length=15)
    stock = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    rem = models.CharField(max_length=10,null=True)
    creationdate = models.DateField(null=True)
    def __str__(self):
        return self.productname

class Supplier(models.Model):
    suppliername = models.CharField(max_length=150)
    suppliermob = models.IntegerField(unique=True)
    supplieraddr = models.TextField()
    supplieremail = models.EmailField()
    categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategoryid = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    def __str__(self):
        return self.suppliername


class Cart(models.Model):
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    billingid = models.CharField(max_length=15)
    productqty = models.CharField(max_length=20)
    ischeckout = models.CharField(max_length=10)
    cartdate = models.DateField(null=True)
    def __str__(self):
        return self.id

class Customer(models.Model):
    billingid = models.CharField(max_length=15)
    customername = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=15)
    modeofpayment = models.CharField(max_length=30)
    billingdate = models.DateField(null=True)
    def __str__(self):
        return self.customername



