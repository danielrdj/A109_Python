#########################################
# Daniel Johnson
# Assignment 4.1
# 3/8/19
#
# Description: This program determines the day of the week for a given date
#
# Inputs: This program takes a day, month, and year (all int) as input
#
# Outputs: This outputs the day of the week that the given date occurred on
#########################################



################################
# Purpose: This function returns
# true if the input year is a
# leap year
# Input: This takes a 4 digit
# year as input
#
# Return/Output: This returns
# a boolean
###############################
def is_leap_year(year):
    if year % 400 == 0:
        return True
    else:
        return False

################################
# Purpose: This function returns
# a value based on the century
#
# Input: This takes a 4 digit
# year as input
#
# Return/Output: This returns
# an int value based on the input
# year
###############################
def get_century_value(year):
    year = str(year)
    temp = year[0] + year[1]
    temp = int(temp)
    temp = (3 - (temp % 4)) * 2
    return temp

################################
# Purpose: This function returns
# a value based on the year
#
# Input: This takes a 4 digit
# year as input
#
# Return/Output: This returns
# an int value based on the input
# year
###############################
def get_year_value(year):
    year = str(year)
    temp = year[-2] + year[-1]
    temp = int(temp)
    temp2 = temp
    temp = (temp // 4)
    temp = temp2 + temp
    return temp


################################
# Purpose: This function returns
# a value based on the month
#
# Input: This takes a 4 digit
# year and a 2 digit month
# as input
#
# Return/Output: This returns
# an int value based on the input
# month and year input
###############################
def get_month_value(month, year):
    if month == 1:
        if is_leap_year(year):
            return 6
        else:
            return 0
    elif month == 2:
        if is_leap_year(year):
            return 2
        else:
            return 3
    elif month == 3:
        return 3
    elif month == 4:
        return 6
    elif month == 5:
        return 1
    elif month == 6:
        return 4
    elif month == 7:
        return 6
    elif month == 8:
        return 2
    elif month == 9:
        return 5
    elif month == 10:
        return 0
    elif month == 11:
        return 3
    elif month == 12:
        return 5
    else:
        print("An invalid answer was input. The program will now end")
        exit(0)





################################
# Purpose: This function returns
# the day of the week for a given
# date
#
# Input: This takes 3 int inputs
# as day, month, and year
#
# Return/Output: This returns
# the day of the week as a string
# based on input
###############################
def get_day_of_week(day, month, year):
    temp = (day + get_month_value(month,year) + get_year_value(year) + get_century_value(year))
    temp = temp % 7
    if temp == 0:
        return "Sunday"
    elif temp == 1:
        return "Monday"
    elif temp == 2:
        return "Tuesday"
    elif temp == 3:
        return "Wednesday"
    elif temp == 4:
        return "Thursday"
    elif temp == 5:
        return "Friday"
    elif temp == 6:
        return "Saturday"
    else:
        return "Something went wrong"




#This uses the above functions to help a user find the day of the week a certain date was
day_val = int(input("Enter the day (as a number): "))
month_val = int(input("Enter the month (as a number): "))
year_val = int(input("Enter the year (as a 4-digit number): "))
print("That day of the week is a", get_day_of_week(day_val, month_val, year_val))