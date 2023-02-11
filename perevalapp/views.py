from django.shortcuts import render
from rest_framework import generics
from .models import pereval_added
from .serializers import PerevalSerializers


class submitData(generics.ListCreateAPIView):
    queryset = pereval_added.objects.all()
    serializer_class = PerevalSerializers


