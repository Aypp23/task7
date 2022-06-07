from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Address(models.Model):
    street_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)

class Bio(models.Model):
    description = models.TextField(max_length=200)

class People(models.Model):
    addresses = models.ManyToManyField(Address)
    person_bio = models.OneToOneField(Bio, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Doctor(models.Model):
    patients = models.ForeignKey(People, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=8, decimal_places=2)


