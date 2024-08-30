from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    name=serializers.CharField(read_only = True)

    class Meta:
      model=Student
    #   fields=['id','name','roll','city']
      fields='__all__'