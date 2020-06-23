from django.db import models


# Create your models here.
class About(models.Model):
        dob=models.DateField(null=False)
        web=models.URLField(null=True)
        phone=models.IntegerField(null=False)
        age=models.IntegerField(null=False)
        degree=models.CharField(max_length=100,null=True)
        email=models.EmailField(null=False)
        freelancing=models.CharField(max_length=200,null=True)
        notes=models.CharField(max_length=800,null=True)
        city=models.CharField(max_length=100,null=True)
        heading=models.CharField(max_length=100,null=True)
        intro=models.CharField(max_length=500,null=True)

class Skills(models.Model):
      skill=models.CharField(max_length=300,null=False)
      percent=models.IntegerField(null=False)

      def __str__(self):
          return self.skill

class Interest(models.Model):
       interest=models.CharField(max_length=500,null=True)



'''class About:
    id = int
    dob: str
    web = str
    phone = str
    city = str
    age = int
    degree = str
    email = str
    freelancing = str


class Skills:
    skill = str
    percent = int


class Interest:
    interest=str'''

