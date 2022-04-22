# -*- coding: utf-8 -*-
import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


# name = input("input your name: ")
# age = input("input your age: ")

year1 = int(input("请输入年份："))
month1 = int(input("请输入月份："))
day1 = int(input("请输入日期："))
localtime = time.localtime(time.time())
leap_year = judge_leap_year(localtime.tm_year)
# print(localtime)

year2 = localtime.tm_year
month2 = localtime.tm_mon
day2 = localtime.tm_mday

year = year2 - year1
# if month2 < month1:
#     month = month2 + 12 - month1
#     year -= 1
# else:
#     month = month1 - month2
# if day2<day1:
#     day = day1+month_days(month1,leap_year) - day2 - 1
#     #month -= 1
# else:
#     day = day2 - day1

# begin_year = int(localtime.tm_year) - year1
# end_year = begin_year + year

day = 0
# calculate the days
if year>0:
    for i in range(month1,13):
        day = day + month_days(i, leap_year)
    for j in range(1,month2):
        day = day + month_days(j, leap_year)
    year -= 1

for y in range(year1, year2):
    if (judge_leap_year(y)) and year>0:
        day = day + 366
        year -= 1
    elif (judge_leap_year(y))==False and year>0:
        day = day + 365
        year -= 1

# for m in range(month1, month2):
#     day = day + month_days(m, leap_year)

day = day + localtime.tm_mday + month_days(month1,leap_year) - day1
#print("%s's age is %d years or " % (name, year), end="")
print("距今 %d 天" %day)
