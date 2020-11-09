from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from course.serializers import CourseSerializer
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def index(request):
    if request.method == "POST":
        serilizer = CourseSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status.HTTP_400_BAD_REQUEST)