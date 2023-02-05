from django.db import models

# Create your models here.


class Degree(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'degree_table'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)

    class Meta:
        db_table = 'department_table'

    def __str__(self):
        return self.name
