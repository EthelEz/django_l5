from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    num_students = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cbv_app:detail", kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=64)
    level = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

# class Course(models.Model):
#     name = models.CharField(max_length=64)
#     level = models.ForeignKey(Student, related_name='courses', on_delete=models.CASCADE,)
#
#     def __str__(self):
#         return self.name
#
# class Teacher(models.Model):
#     name = models.CharField(max_length=64)
#     # course = models.CharField(max_length=64)
#     course = models.ForeignKey(Course, related_name='teachers', on_delete=models.CASCADE,)
#
#     def __str__(self):
#         return self.name
