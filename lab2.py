# If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
# “mAHA bHARAT”
# “Bharat”
# “BharatBharatBharat”
# “Mera Bharat”
# “Mera Bharat Mahan”

def manipulate_string(s1):
    print(s1.swapcase())
    print(s1[5:])
    print(s1[5:]*3)
    print("Mera", s1[5:])
    print("Mera", s1[5:], "Mahan")

s1 = "Maha Bharat"
manipulate_string(s1)

# For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
# The length of the string S
# The first occurrence of the letter ‘e’
# The total number of occurrences of ‘a’
# Generate “Ta Ta Black Sheep”


def manipulate_string(s):
    print(len(s))
    print(s.find('e'))
    print(s.count('a'))
    print(s.replace('Ba', 'Ta'))

s = "Ba Ba Black Sheep"
manipulate_string(s)

# Write a python script to enter any string at run time and check whether it is a palindrome or not.

def check_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

s = input("Enter a string: ")
check_palindrome(s)

# Enter the following details of a student at run time: - Name, Roll number and marks secured for Mathematics Examination out of 100. Write a python script to display student details as shown:
# Name:
# Roll Number:
# Marks:
# Grade Point:
# Remark:

def student_details():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")
    marks = int(input("Enter Marks: "))
    if marks >= 90:
        grade_point = 10
        remark = "Outstanding"
    elif marks >= 80:
        grade_point = 9
        remark = "Very Good"
    elif marks >= 70:
        grade_point = 8
        remark = "Good"
    elif marks >= 60:
        grade_point = 7
        remark = "Average"
    elif marks >= 50:
        grade_point = 6
        remark = "Pass"
    else:
        grade_point = 0
        remark = "Fail"
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Marks:", marks)
    print("Grade Point:", grade_point)
    print("Remark:", remark)


student_details()


# Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)


def find_roots(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print("Roots are:", root1, root2)
    elif d == 0:
        root = -b / (2*a)
        print("Both Roots are:", root)
    else:
        real_part = -b / (2*a)
        imaginary_part = (-d)**0.5 / (2*a)
        print("Roots are:", real_part, "+", imaginary_part, "and", "i", real_part, "-", imaginary_part, "i")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
find_roots(a, b, c)