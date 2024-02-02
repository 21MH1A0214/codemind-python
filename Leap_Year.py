year=int(input())
if (year % 400 == 0) and (year % 100 == 0):
    print("Leap Year")

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("Leap Year")

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("Not Leap Year")