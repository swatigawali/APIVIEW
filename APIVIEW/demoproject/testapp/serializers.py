from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Employee


def multiple_of_1000(value):
    #validation by using validators
    print('Validation using validators field')
    if value %1000 !=0:
        raise serializers.ValidationError("salary should be in multiple of 1000")


class EmployeeSerializer(serializers.ModelSerializer):
    emp_sal=serializers.FloatField(validators=[multiple_of_1000,])
    class Meta:
        model=Employee
        fields="__all__"
