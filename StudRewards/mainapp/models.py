from django.db import models


class Student(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
    course = models.IntegerField()


class Teacher(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=60)


class Activity(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    units = models.IntegerField()
    students = models.ManyToManyField(Student)


class Report(models.Model):
    description = models.CharField(max_length=20)
    date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    checked = models.IntegerField()
    students = models.ManyToManyField(Student)
