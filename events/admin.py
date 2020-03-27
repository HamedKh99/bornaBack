from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class HaftkhanSignupResource(resources.ModelResource):
    class Meta:
        model = HaftkhanSignup


class HaftkhanSignupAdmin(ImportExportModelAdmin):
    resource_class = HaftkhanSignupResource


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student


class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource


admin.site.register(HaftkhanPre)
admin.site.register(HaftkhanSignup, HaftkhanSignupAdmin)
admin.site.register(Student, StudentAdmin)
