from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
       if pk is not None:
            try:
               stu=Student.objects.get(id=pk)
               serializer=StudentSerializer(stu)
               print(serializer.data)
               return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
       stu=Student.objects.all()
       serializer=StudentSerializer(stu,many=True)
       return Response(serializer.data)
        
    if request.method == "POST":
        data=request.data
        serializer=StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data save in db '})
        return Response(serializer.errors)
    
    if request.method == "PUT":
        data=request.data
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Update in db '})
        return Response(serializer.errors)
    
    if request.method == "PATCH":
        data=request.data
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Update in db '})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Data delete in db '})
        return Response(serializer.errors)
        
    