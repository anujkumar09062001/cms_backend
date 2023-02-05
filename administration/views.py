from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404

# Create your views here.


class DegreeList(ListAPIView):
    serializer_class = DegreeSerializer

    def get_queryset(self):
        degree_list = Degree.objects.all().order_by('name')
        return degree_list

    def post(self, request, format=None):
        serializer = DegreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DegreeDetail(APIView):
    def get_object(self, pk):
        try:
            return Degree.objects.get(pk=pk)
        except Degree.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        degree = self.get_object(pk)
        serializer = DegreeSerializer(degree)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        degree = self.get_object(pk)
        serializer = DegreeSerializer(degree, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        degree = self.get_object(pk)
        degree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentList(ListAPIView):
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['degree']

    def get_queryset(self):
        department_list = Department.objects.all().order_by('name')
        return department_list

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(
            department, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
