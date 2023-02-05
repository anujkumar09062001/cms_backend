from django.shortcuts import render
from .models import Hostel
from .serializers import HostelSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class HostelList(ListAPIView):
    serializer_class = HostelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

    def get_queryset(self):
        hostel_list = Hostel.objects.all()
        return hostel_list

    def post(self, request, format=None):
        serializer = HostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HostelDetail(APIView):
    def get_object(self, pk):
        try:
            return Hostel.objects.get(pk=pk)
        except Hostel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hostel = self.get_object(pk)
        serializer = HostelSerializer(hostel)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hostel = self.get_object(pk)
        serializer = HostelSerializer(hostel, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hostel = self.get_object(pk)
        hostel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
