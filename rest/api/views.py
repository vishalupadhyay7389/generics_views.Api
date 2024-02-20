from django.shortcuts import render
from .models import Student , StudentSerlizer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class StudentDetailView(generics.ListAPIView , generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerlizer
    
class StudentDeatilListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerlizer
    