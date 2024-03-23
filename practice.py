# import datetime

# def current_week_of_month(date):
#     first_day_of_month = date.replace(day=1)
#     first_day_of_month_weekday = first_day_of_month.weekday()
#     offset = (date.day + first_day_of_month_weekday - 1) // 7
#     return offset + 1

# # Get the current date
# current_date = datetime.datetime.now()

# # Print the current week of the month
# print("Current week of the month:", current_week_of_month(current_date))



import datetime
# Get the current date
current_date = datetime.datetime.now()
# Get the day of the week (Monday is 0 and Sunday is 6)
current_day_of_week = current_date.weekday()
print(current_day_of_week)