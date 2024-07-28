from django.db import models
# from django.db import models



CHOICE_GENDER=(
   ("Male","male"),
   ("Female","female"),
   ("other","others")
)
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30,null=True)
    age=models.IntegerField()
    email=models.EmailField(max_length=20)
    gender=models.CharField(max_length=10,choices=CHOICE_GENDER)
    

    def __str__(self):
       return f" {self.name} + {self.email} {self.gender} "

