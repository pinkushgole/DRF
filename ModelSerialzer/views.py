from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import *
from .serializer import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentM(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)

        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            st=Student.objects.all()
            serializer=StudentSerializer(st,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
    
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)

        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data,partial=True)
        
        if serializer.is_valid():
          serializer.save()
          res={'msg':'Data Update'}
          json_data=JSONRenderer().render(res)
          return HttpResponse(json_data,content_type='application/json')


    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)

        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Delete'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    

        
   
    
        