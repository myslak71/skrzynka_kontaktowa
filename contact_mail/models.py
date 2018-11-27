from django.db import models


# Create your models here.


class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building_number = models.CharField(max_length=50)
    apartment_number = models.CharField(max_length=50)


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='user_images')
    address = models.ForeignKey(Address, models.SET_NULL, null=True)
    group = models.ManyToManyField('Group')


PHONE_CHOICES = (
    (0, 'mobile'),
    (1, 'company'),
    (2, 'home'),
)


class Phone(models.Model):
    number = models.IntegerField(null=True)
    type = models.SmallIntegerField(choices=PHONE_CHOICES)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


EMAIL_CHOICES = (
    (0, 'private'),
    (1, 'company'),
)


class Email(models.Model):
    address = models.EmailField(max_length=254)
    type = models.SmallIntegerField(choices=EMAIL_CHOICES)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=254)
