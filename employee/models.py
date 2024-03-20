from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, related_name = "employee_detail")
    salary = models.DecimalField(max_digits = 9,null=False, decimal_places=2)
    deduction_amount = models.DecimalField(max_digits = 9, null=False, decimal_places=2)
    image = models.ImageField(null=False, blank=True,upload_to="uploads/images/")

    def __str__(self):
        user = User.objects.filter(username=self.user)
        return user[0].username


class DailyRegister(models.Model):
    employee_id = models.ForeignKey(User,on_delete = models.CASCADE, related_name = "daily_attendance")
    date = models.DateField(null=False, blank=False)
    in_time = models.TimeField(null=False, blank=False)
    out_time = models.TimeField(null=True)
    hours = models.DurationField(null=True)

month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


class MonthlyRegister(models.Model):
    employee_id = models.ForeignKey(User,on_delete = models.CASCADE, related_name = "monthly_attendance")
    total_presents = models.IntegerField(default=0)
    total_absents = models.IntegerField(default=0)
    year = models.IntegerField(null = False)
    month = models.IntegerField(null = False)

    def __str__(self):
        return month_dict[self.month]