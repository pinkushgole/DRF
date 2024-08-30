from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer


# Create your views here.

class StudentClassApi(APIView):
    def get(self,request,pk=None,format=None):
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


    def post(self,request,format=None):
        data=request.data
        serializer=StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data save in db '})
        return Response(serializer.errors)
        
    def put(self,request,pk,format=None):
        data=request.data
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Update in db '})
        return Response(serializer.errors)
        
    def patch(self,request,pk,format=None):
        data=request.data
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Update in db '})
        return Response(serializer.errors)
        
    
    def delete(self,request,pk,format=None):
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Data delete in db '})
        return Response(serializer.errors)
        
    