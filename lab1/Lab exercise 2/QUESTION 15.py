#Check weather the given year is leap year or not .If year is leap print 'LEAP YEAR' else print 'COMMON YEAR'
#HINT: a year is a leap year if its number is exactely divisible by 4 and is not exactly divisible by 100
#    : a year is always a leap year if its number is exactely divisible by 400.
'''year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} IS LEAP YEAR".format(year))
else:
   print("{0} IS COMMON YEAR".format(year))'''

year=int(input('enter year to be checked'))
if(year%4==0 and year % 100 !=0 or year % 400 ==0):
else:
    print("The year isn't a leap year!")