from django.db import models
from django.core.exceptions import ValidationError


class Heading(models.Model):
    title = models.CharField(max_length=100)
    motto = models.CharField(max_length=200)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if Heading.objects.exists():
    #         raise ValidationError('Heading Already Exists!')
    #     return super(Heading, self).save(force_insert, force_update, using, update_fields)


class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link_to = models.CharField(max_length=100)


class ContactUs(models.Model):
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if ContactUs.objects.exists():
    #         raise ValidationError('ContactUs Already Exists!')
    #     return super(ContactUs, self).save(force_insert, force_update, using, update_fields)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)