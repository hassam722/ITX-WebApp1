from django.contrib import admin
from .models import Employee,DailyRegister,MonthlyRegister

# Register your models here.

admin.site.register(Employee)
admin.site.register(DailyRegister)
admin.site.register(MonthlyRegister)
