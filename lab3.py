# 1. Write a python script to find the squares of first n natural numbers. 
# Display both the number and the square as shown below. Use while loop
n = int(input("Enter the number: "))
i=1 
while(i<=n):
    print(i, ":", i*i)
    i+=1

# 2. Write a python script to find the sum of the digits of the given number using a while loop. 
# Display the number and the sum.
n= int(input("Enter the number: "))
m=n
sum=0
while(n>0):
    d=n%10
    sum+=d
    n=n//10
print("Sum of digits of", m , "is: ", sum)

#3. Write a python script to print the first n terms of the Fibonacci series using while loop
n= int(input("Enter the number: "))
a=0
b=1
i=0
while(i<n):
    i=i+1
    print(a)
    c=a+b
    a=b
    b=c


#4. Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.
n= int(input("Enter the number: "))
l=int (input("Enter the limit: "))
i=1
while(i<=l):
    print(n, "*", i, "=", n*i)
    i+=1

# 5. Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for. 
# Print True if all characters are alphanumeric. Otherwise print False.
a=input("Enter the string: ")
if(a.isalnum()):
    print("True, The string is alphanumeric")
else:
    print("False, The string is not alphanumeric")

# 6. Write a python script to find the number of occurrences of a particular character present in the given string using a loop. (Don’t use string methods).
s=input("Enter the string: ")
c=input("Enter the character to be counted: ")
count=0
for i in s:
    if i==c:
        count+=1
print(c, "is present", count , "times in", s)