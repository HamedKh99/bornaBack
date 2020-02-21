from rest_framework import views
from rest_framework.response import Response

from .models import *
from .serializers import *


class HomepageView(views.APIView):
    def get(self, request, format=None, **kwargs):
        heading_serializer = HeadingSerializer(Heading.objects.first())
        section_serializer = SectionSerializer(Section.objects.all(), many=True)
        contact_us_serializer = ContactUsSerializer(ContactUs.objects.first())
        social_network_serializer = SocialNetworkSerializer(SocialNetwork.objects.all(), many=True)

        return Response({
            'heading': heading_serializer.data,
            'sections': section_serializer.data,
            'contact_us': contact_us_serializer.data,
            'social_networks': social_network_serializer.data
        })
