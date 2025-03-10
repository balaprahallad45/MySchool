from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    # ... other fields

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    # ... other fields

    def __str__(self):
        return self.name

