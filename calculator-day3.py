#int data type
#simple calculator program#     # Day 3 - 11/02/2026  
###Type Casting

# type 1- type casting

x = input("Enter x: ")      
y = input("Enter y: ")              #int

z = int(x)+int(y)

print(z)

###################################################

# type 2

x1 = int(input("Enter x: "))          #int
y1 = int(input("Enter y: "))

z1 = x1+y1

print(z1)

####################################################

#Type 3 

x2 = float(input("Enter x: "))          #float(decimal)
y2 = float(input("Enter y: "))

z2 = x2+y2

print(z2)

#####################################################

#rounding decimal

x3 = float(input("Enter x: "))          #round
y3 = float(input("Enter y: "))

z3 = round(x3+y3)

print(f"{z3:,}")   #comma as thousand separator