def is_leap_year(year):
    if year % 400 == 0:
        return True
    else:
        return False

'''
This function should return True if year is a leap year and False if it is not. Here is
pseudocode to determine a leap year:
year is a leap year if ((year is divisible by 400) or (year is divisible by 4 and year is not
divisible by 100))
'''
def get_century_value(year):
    year = str(year)
    temp = year[0] + year[1]
    temp = int(temp)
    temp = (3 - (temp % 4)) * 2
    return temp

'''
This function should take the first two digits of the year (i.e. the century - you can get this
using integer division), divide by 4, and save the remainder. Subtract the remainder from 3
and return this value multiplied by 2. For example, the year 2011 becomes: (20/4) = 5
remainder 0. 3 - 0 = 3. Return 3 * 2 = 6.
'''
def get_year_value(year):
    year = str(year)
    temp = year[-2] + year[-1]
    temp = int(temp)
    temp2 = temp
    temp = (temp // 4)
    temp = temp2 + temp
    return temp
'''
This function computes a value based on the years since the beginning of the century. First,
extract the last two digits of the year (use modulus). For example, 11 is extracted for
2011. Divide the resulting value by 4 and discard the remainder. Add the two results
together and return this value. For example, from 2011 we extract 11. Then (11/4) = 2
remainder 3. Return 2 + 11 = 13.
'''
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

def get_day_of_week():
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

day = int(input("Enter the day (as a number): "))
month = int(input("Enter the month (as a number): "))
year = int(input("Enter the year (as a 4-digit number): "))
print("That day of the week is a", get_day_of_week())