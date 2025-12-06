# Determining the number of days in a month (leap year aware).
# Author: Maleka Tumisho Mmatlou
# Date : 06 December 2025

# Checking whether it's a leap year:
def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or  year % 400 == 0
def main():
    # Getting inputs
    month = int(input("Enter number of month (1 is January):\n"))
    year = int(input("Enter year:\n"))

    # Inserting months in a list
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']

    # Assigning each month with its corresponding number of days:
    days = { 1:31 ,2:28, 3 :31, 4:30, 5:31, 6: 30, 7:31, 8 : 31, 9:30, 10:31, 11:30, 12:31}

   #Output:
    if leap_year(year) :
        days.update({2 : '29'})
     

    print('In the year {}, {} has {} days.'.format(year,months[month-1],days[month]))

main()