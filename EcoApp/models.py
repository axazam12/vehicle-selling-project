from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_dealer = models.BooleanField(default=False)
    is_authority = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='customer')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='profile',null=True)
    approval_status = models.BooleanField(default=0)

class Dealer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='dealer')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='profile',null=True)
    approval_status = models.BooleanField(default=0)

class Authority(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='authority')
    name = models.CharField(max_length=50)
    office_address = models.CharField(max_length=100)
    email = models.EmailField()
    office_phone_no = models.CharField(max_length=10)
    approval_status = models.BooleanField(default=0)

Type=(
    ('Car','Car'),
    ('Bike','Bike'),
    ('Auto','Auto'),
    ('Traveller','Traveller'),
    ('Taxi','Taxi'),
    ('Bus','Bus')
)
Fuel=(
    ('Petrol','Petrol'),
    ('Disel','Disel'),
    ('CNG','CNG')
)

class Scrap(models.Model):
    vehicle_type=models.CharField(max_length=100,choices=Type)
    vahicle_name=models.CharField(max_length=100)
    Fuel_Type=models.CharField(max_length=100,choices=Fuel)
    photo=models.ImageField(upload_to='scrap')
    Expected_amount=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Phone_No=models.CharField(max_length=10)
    approval_status=models.BooleanField(default=0)


