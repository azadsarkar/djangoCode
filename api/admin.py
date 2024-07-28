from django.contrib import admin
from django.contrib.auth.models import User
from api.models import Student

# Register your models here.
@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display=["name","email","age","gender"]