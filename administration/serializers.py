from rest_framework import serializers
from .models import *


class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degree
        fields = ('__all__')


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('__all__')
