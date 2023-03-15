from django.db import models

# Create your models here.
class Course(models.Model):
    course_type = models.CharField(max_length=50)

    def __str__(self):
         return f'{self.course_type}'

class City(models.Model):
    City_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.City_name}'
class Student(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_age = models.IntegerField()
    stud_phno = models.BigIntegerField()
    stud_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_city = models.ForeignKey(City, on_delete=models.CASCADE)

