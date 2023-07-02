from datetime import date
import calendar

today = date.today()

day_today = today.day
month_number = today.month
month_name = calendar.month_name[month_number]
