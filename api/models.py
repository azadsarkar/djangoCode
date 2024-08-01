from django.db import models
# from django.db import models

CHOICE_GENDER=(
   ("Male","male"),
   ("Female","female"),
   ("other","others")
)
class BaseModel(models.Model):
   name=models.CharField(max_length=30, null=True)
   last_name=models.CharField(max_length=30,null=True)
   age=models.IntegerField(null=True)
   email=models.EmailField(max_length=20,null=True)
   gender=models.CharField(max_length=10,choices=CHOICE_GENDER,null=True)


class StudentCommon(BaseModel):
   school_name = models.CharField(max_length=30)
   school_place = models.CharField(max_length=30)
   school_code  = models.CharField(max_length=30)
   
   def __str__(self) -> str:
      return f"{self.school_name}==={self.school_place}"


class StudentProfile(models.Model):
    
   student = models.OneToOneField(StudentCommon, on_delete=models.CASCADE)
   enroll_code  = models.CharField(max_length=30)
   village =  models.CharField(max_length=30)
    

class Subject(models.Model):
   subject_name = models.CharField(max_length=30)

   def __str__(self) -> str:
      return self.subject_name


class StudentSubject(models.Model):
   student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

   class Meta:
       unique_together = ("student", "subject") # uniqe_together student name or subject name ak bar hi same ho sakta 
                                                #hai ager student name or subject do bar same ho to bo arre provede kar dega
   print("jhdfgsuh")