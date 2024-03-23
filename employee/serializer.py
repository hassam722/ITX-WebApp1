from rest_framework import serializers
from .models import Employee,MonthlyRegister,DailyRegister
from datetime import datetime,timedelta

class DailySerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    class Meta:
        model = DailyRegister
        fields = ['in_time','out_time','hours','day']
    
    def get_day(self,obj):
        return obj.date.strftime('%A')


class EmployeeSerializer(serializers.ModelSerializer):
    TotalPresents = serializers.SerializerMethodField()
    TotalAbsents = serializers.SerializerMethodField()
    Deduction = serializers.SerializerMethodField()
    Payable = serializers.SerializerMethodField()
    WeekData = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['TotalPresents', 'TotalAbsents', 'Deduction', 'Payable','WeekData']
        
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
    
    def get_WeekData(self,obj):
        
        current_date = datetime.now()
        monday_date = current_date - timedelta(days=current_date.weekday())
        friday_date = monday_date + timedelta(days = 4)
        daily_objs =  DailyRegister.objects.filter(date__range=[monday_date, friday_date])
        daily_serializer = DailySerializer(daily_objs,many = True)
        return daily_serializer.data