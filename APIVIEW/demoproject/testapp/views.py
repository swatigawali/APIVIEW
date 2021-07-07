from django.http import response
import rest_framework
from rest_framework.serializers import Serializer
from .models import Employee
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
# Create your views here.

class EmployeeAPIview(APIView):
    def get(self,request,pk=None):
        id=pk
        if id is not None:
            emp=Employee.objects.get(id=id)
            serializer=EmployeeSerializer(emp)
            return Response(serializer.data)
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Employee added successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        id=pk
        emp=Employee.objects.get(pk=id)
        serializer=EmployeeSerializer(instance=emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data updated successfully"})
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
        id=pk
        emp=Employee.objects.get(pk=id)
        emp.delete()
        return Response({"msg":"Data deleted"})
        




