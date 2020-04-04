from django.db import models
from django.core.exceptions import ValidationError


class Heading(models.Model):
    title = models.CharField(max_length=100)
    motto = models.CharField(max_length=200)


class Introduction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/')


class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link_to = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class ContactUs(models.Model):
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)