# euler problem 19
#   Matthew Huber, 3-25-2013

# Counting Sundays
# Problem 19
# 
# You are given the following information, but you may prefer to do 
# some research for yourself.
# 
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on 
#   a century unless it is divisible by 400.
# 
# How many Sundays fell on the first of the month during the twentieth 
# century (1 Jan 1901 to 31 Dec 2000)?


# 1 Jan 1901 was a Tuesday

monthLength = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#dayNames = ["Mon","Tue","Wed","Thurs","Fri","Sat","Sun"]

def iterateYears():
    monthDay = 1
    weekDay = 2
    month = 1
    year = 1901
    totalSundays = 0
    while year < 2001:
        if weekDay == 7 and monthDay == 1: 
            totalSundays += 1

        weekDay += 1
        if weekDay > 7: 
            weekDay = 1

        monthDay += 1
        if year % 4 == 0 and month == 2: #Feb in leap year
            if year % 100 == 0 and year % 400 == 0 and monthDay > 29: #century
                monthDay = 1
                month += 1
            elif monthDay > 29:
                monthDay = 1
                month += 1

        elif monthDay > monthLength[month]: 
            monthDay = 1
            month += 1

        if month > 12:
            month = 1
            year += 1



    return totalSundays


print( iterateYears() )

        


