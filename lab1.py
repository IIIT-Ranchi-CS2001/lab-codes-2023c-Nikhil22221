# Write a program to find the: Sum, Difference,   Product,  Integer quotient,Remainder, Fractional quotient

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Sum: ", a+b)
print("Difference: ", a-b)
print("Product: ", a*b)
print("Integer quotient: ", a//b)
print("Remainder: ", a%b)
print("Fractional quotient: ", a/b)

# Write python program to find
# (a) Area and perimeter of a triangle when all three sides are given. Hint: (Use Heron’s Equation)
# (b) Find all three angles of the triangle


import math
a= int(input("Enter the first side of the triangle: "))
b= int(input("Enter the second side of the triangle: "))
c= int(input("Enter the third side of the triangle: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
perimeter = a+b+c
print("Area of the triangle: ", area)
print("Perimeter of the triangle: ", perimeter)

angleA = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
angleB = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
angleC = math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
print("Angle A: ", angleA)
print("Angle B: ", angleB)
print("Angle C: ", angleC)

# Write a program to find:
# The equivalent impedance when two impedances Z1 and Z2 are connected in parallel. 
# Display Z1 and Z2 in complex form. 
# Display the real part and imaginary part of the result in separate lines.

import cmath
z1 = complex(input("Enter the first impedance: "))
z2 = complex(input("Enter the second impedance: "))
z = 1/((1/z1) + (1/z2))
print("Z1: ", z1)
print("Z2: ", z2)
print("Real part of the equivalent impedance: ", z.real)
print("Imaginary part of the equivalent impedance: ", z.imag)