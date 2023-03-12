from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Students

def index(r):
    return "hello"

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class MyStudentsView(APIView):
    def get(self, request, id=-1):  # axios.get
        if int(id) > -1:
            my_model = Students.objects.get(id=id)
            serializer = StudentsSerializer(my_model, many=False)
        else:
            my_model = Students.objects.all()
            serializer = StudentsSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):  # axios.post
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):  # axios.put
        my_model = Students.objects.get(id=id)
        serializer = StudentsSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):  # axios.delete
        my_model = Students.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)