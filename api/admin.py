from django.contrib import admin
from django.contrib.auth.models import User
from api.models import *


# studentcommon ke andr hi studentprole ko add kr skte hai tabular form me
# @admin.register(StudentProfile)
class StudentProfileAdmin(admin.TabularInline):
    model = StudentProfile

@admin.register(StudentCommon)
class StudentCommonAdmin(admin.ModelAdmin):
    list_display=["name","last_name","school_name","school_code"]
    inlines = [StudentProfileAdmin] # StudentProfile instance , StudentCommon model ke andr hi show hoga admin pannel pr 
    

@admin.register(Subject)
class StudentAdmin(admin.ModelAdmin):
    list_display=["subject_name"]
    
@admin.register(StudentSubject)
class StudentAdmin(admin.ModelAdmin):
    list_display=["student", "subject"]
    