from rest_framework import serializers
from .models import Employee,MonthlyRegister,DailyRegister
from datetime import datetime

class EmployeeSerializer(serializers.ModelSerializer):
    TotalPresents = serializers.SerializerMethodField()
    TotalAbsents = serializers.SerializerMethodField()
    Deduction = serializers.SerializerMethodField()
    Payable = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = ['TotalPresents', 'TotalAbsents', 'Deduction', 'Payable']
        
    def get_MonthObj(self,obj):
        month = datetime.now()
        month = month.strftime('%m')
        month_obj = MonthlyRegister.objects.get(employee_id=obj.user_id,month = month)
        return month_obj
    def get_TotalPresents(self,obj):
        return self.get_MonthObj(obj).total_presents
    
    def get_TotalAbsents(self,obj):
        return self.get_MonthObj(obj).total_absents
    
    def get_Deduction(self,obj):
        return self.get_MonthObj(obj).total_absents * obj.deduction_amount
    
    def get_Payable(self,obj):
        return obj.salary - self.get_Deduction(obj)