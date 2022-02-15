from django.db import models

# Create your models here.
# class Todo(models.Model):
#     text = models.CharField(max_length=40)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.text


class Computer_First(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name

class Computer_Second(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name

class Computer_Third(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name


class Computer_Fourth(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name

class Electrical_First(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name

class Electrical_Second(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name
class Electrical_Third(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name
class Electrical_Fourth(models.Model):
    batch = models.CharField(max_length = 20)
    semester = models.CharField(max_length = 20)
    Lecturer_Name = models.CharField(max_length = 50, blank=True, default=None)
    Lecturer_Code = models.SlugField(max_length = 10)
    Lecturer_Id = models.IntegerField(primary_key = True)
    Lecturer_Subject = models.CharField(max_length = 100, blank=True, default=None)
    Lecturer_Period = models.IntegerField(default=0)
    Lab_Class = models.CharField(max_length = 10)
    Lab_Period = models.IntegerField()

    def __str__(self):
        return self .Lecturer_Name