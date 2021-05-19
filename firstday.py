year = int( input("Enter the year: "))


import math

a = (year-1)%4
b = (year-1)%100
c = (year-1)%400
d = 1 + (5*a) + (4*b) + (6*c)
day = d%7

print("The 1st of January" , year ,"falls on day" , day , "of the week (0=Sun, ..., 6=Sat).")