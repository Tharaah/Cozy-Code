import math
a=input("Enter the length of the first side: ")
b=input("Enter the length of the second side: ")
c=input("Enter the length of the third side: ")

a = float(a)
b = float(b)
c = float(c)
s=(a+b+c)/2
Area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of the triangle with sides of length", int(a) , "and", int(b), "and", int(c), "is "+ str(Area) +".")