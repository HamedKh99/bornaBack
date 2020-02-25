from django.db import models


class HaftkhanPre(models.Model):
    description = models.TextField()
    video = models.FileField(upload_to='videos/')


class HaftkhanSignup(models.Model):
    complex_name = models.CharField(max_length=200)
    state_name = models.CharField(max_length=200)
    city_name = models.CharField(max_length=200)
    full_address = models.TextField()
    complex_phone_number = models.CharField(max_length=200)
    is_from_kanoon_imam_reza = models.BooleanField()
    head_name = models.CharField(max_length=200)
    head_family_name = models.CharField(max_length=200)
    head_phone_number = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200)
    teacher_family_name = models.CharField(max_length=200)
    teacher_education = models.CharField(max_length=200)
    teacher_phone_number = models.CharField(max_length=200)


class Student(models.Model):
    name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)
    ref_to_form = models.ForeignKey(to=HaftkhanSignup, on_delete=models.CASCADE)