from rest_framework import serializers
from . import models


class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Heading
        fields = ['id', 'title', 'motto']


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Introduction
        fields = ['id', 'title', 'description', 'logo']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Section
        fields = ['id', 'title', 'description', 'image', 'link_to']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = ['id', 'email', 'phone_number']


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialNetwork
        fields = ['id', 'name', 'user_id']
