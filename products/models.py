import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    def __str__(self):
        return self.last_name + " " + self.first_name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/', null=True, blank=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='static/', null=True, blank=True)
    price_1_session = models.CharField(max_length=255)
    price_5_session = models.CharField(max_length=255)
    price_10_session = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Cart(models.Model):
    STATUS = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='open')



class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Appointment(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    duration = models.DurationField(default=datetime.timedelta(hours=1))

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    message = models.TextField()
