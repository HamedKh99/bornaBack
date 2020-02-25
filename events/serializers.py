from rest_framework import serializers
from .models import *


class HaftkhanPreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HaftkhanPre
        fields = ['id', 'description', 'video']


class HaftkhanSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = HaftkhanSignup
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
