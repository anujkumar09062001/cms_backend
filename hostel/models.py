from django.db import models

# Create your models here.


class Hostel(models.Model):
    hostel_type = (
        ('boys', 'BOYS'),
        ('girls', 'GIRLS'),
        ('married', 'MARRIED'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=hostel_type)

    class Meta:
        db_table = 'hostel_table'

    def __str__(self):
        return self.name
