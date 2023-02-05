from django.db import models
from hostel.models import Hostel
from administration.models import *

# Create your models here.


class Student(models.Model):
    gender = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER'),
    )
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=gender)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT)

    class Meta:
        db_table = 'student_table'

    def __str__(self):
        return self.name
