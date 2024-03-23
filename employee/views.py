from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer
# Create your views here.

class EmployeeView(APIView):
    def get(self, request,pk):
        employee = Employee.objects.get(user_id = pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)