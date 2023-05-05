from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=100)
    housenumber = models.IntegerField(default=1)
    street = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ", " + str(self.housenumber) + ", " + self.street + ", "+ self.state + ", " + self.zip + ", "+ self.country

class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
# Create your models here.

class Product(models.Model):
    pname = models.CharField(max_length=100)
    pdescription = models.CharField(max_length=100)
    pimagepath = models.CharField(max_length=100)
    pcategory = models.CharField(max_length=20)
    pprice = models.FloatField()

