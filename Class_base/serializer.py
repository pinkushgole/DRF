from rest_framework import serializers
from .models import *

# validators
def start_with_a(value):
    if value[0].lower() !='a':
        raise serializers.ValidationError("name start with  only  a letter not for other")
    


class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[start_with_a])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    def update(self,instance,validate_data):
        print(instance.name)
        instance.name=validate_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance
    
    # field level validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError("Roll Number More than 200")
        return value
    
    # boject level validation
    def validate(self, data): 
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='vijay' and ct.lower()=='bhopal':
          raise serializers.ValidationError("City must be bhopal")
        return data