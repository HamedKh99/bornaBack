from rest_framework import views, permissions
from rest_framework.response import Response

from .models import *
from .serializers import *


class HaftkhanPreView(views.APIView):
    def get(self, request, format=None, **kwargs):
        haftkhan_pre_serializer = HaftkhanPreSerializer(HaftkhanPre.objects.first())

        return Response({
            'haftkhan_pre': haftkhan_pre_serializer.data
        })


class HaftkhanSignupView(views.APIView):
    permission_classes = permissions.AllowAny

    def post(self, request):
        print(request.data)
        new_signup = HaftkhanSignup(complex_name=request.data['complex_name'], state_name=request.data['state_name'],
                                    city_name=request.data['city_name'], full_address=request.data['full_address'],
                                    complex_phone_number=request.data['complex_phone_number'],
                                    is_from_kanoon_imam_reza=request.data['is_from_kanoon_imam_reza'],
                                    head_name=request.data['head_name'], head_family_name=request.data['head_family_name'],
                                    head_phone_number=request.data['head_phone_number'],
                                    teacher_name=request.data['teacher_name'], teacher_family_name=request.data['teacher_family_name'],
                                    teacher_education=request.data['teacher_education'],teacher_phone_number=request.data['teacher_phone_number']
                                    )
        new_signup.save()
        students = request.data['students']
        for i in range(len(students)):
            if students[i]['name'] != '' and students[i]['family_name'] != '':
                new_student = Student(name=students[i]['name'], family_name=students[i]['family_name'],
                                      school_name=students[i]['school_name'], ref_to_form=new_signup)
                new_student.save()
        return Response({
            'status_code': 200
        })
