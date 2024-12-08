
# Q1 Show party wise seat share for following results of the Assembly Elections 2023 in
# Two different pie charts on two different plots. Party with highest percentage should be shown as slightly detached ( show the percentage seat share on each wedge )
# Two pie charts as subplots on the same figure object
# As a bar chart with party name on X axis and seats won on y axis. Show results of both the states on the same bar plot. Give proper legends
# Madhya Pradesh
# BJP - Win (163) INC - Win (66) BSP – Win ( 0) Others – Win (1)
# Rajasthan
# INC - Win (69) BJP- Win (115) BSP- Win (2) Others-Win (13)

import matplotlib.pyplot as plt

# Madhya Pradesh
labels = ['BJP', 'INC', 'BSP', 'Others']
sizes = [163, 66, 0, 1]
explode = (0.1, 0, 0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.title('Madhya Pradesh')
plt.show()

# Rajasthan
labels = ['INC', 'BJP', 'BSP', 'Others']
sizes = [69, 115, 2, 13]
explode = (0, 0.1, 0, 0)
fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')
plt.title('Rajasthan')
plt.show()


# Bar Chart
labels = ['BJP', 'INC', 'BSP', 'Others']
mp = [163, 66, 0, 1]    
rj = [115, 69, 2, 13]
x = range(len(labels))
fig3, ax3 = plt.subplots()
ax3.bar(x, mp, width=0.4, label='Madhya Pradesh', align='center')
ax3.bar(x, rj, width=0.4, label='Rajasthan', align='edge')
plt.xticks(x, labels)
plt.legend()
plt.title('Madhya Pradesh vs Rajasthan')
plt.show()


# Output
# Pie chart for Madhya Pradesh
# Pie chart for Rajasthan
# Bar chart for both states


k=int(input("Enter the number of values (min. 10)"))
n=int(input("Enter the maximum value till where numbers are to be generated"))
import random
all_numbers=[]
if(k<10):
    print("Please enter a number greater than 10")
    exit()
for i in range(k):
    all_numbers.append(random.randint(1,n))
print(all_numbers)



#  Write a python script to
# Form a list of K random numbers within a limit N where K and N are set by the user. Minimum value of K should be 10.
# Define a function (or two functions) to return the composite numbers and prime numbers of this list as two separate lists.
# Determine the square of all prime numbers and square root of all composite numbers
# Plot both prime numbers Vs their squares and composites Vs their square roots on the same figure object as scatterplots. ( two different subplots on the same figure object)
def check_prime():
    prime_numbers=[]
    composite_numbers=[]
    for i in all_numbers:
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    composite_numbers.append(i)
                    break
            else:
                prime_numbers.append(i)

    return prime_numbers,composite_numbers


def make_square(prime_numbers):
    square_prime=[]
    for i in prime_numbers:
        square_prime.append(i**2)
    return square_prime

def make_squareroot(composite_numbers):
    square_root_composite=[]
    for i in composite_numbers:
        square_root_composite.append(i**0.5)
    return square_root_composite


prime_numbers,composite_numbers=check_prime()

squared_prime_numbers=make_square(prime_numbers)
square_root_composite_numbers=make_squareroot(composite_numbers)



import matplotlib.pyplot as plt
import numpy as np


x=np.array(prime_numbers)
y=np.array(squared_prime_numbers)

plt.subplot(1, 2, 1)
plt.scatter(x,y)
plt.xlabel("Prime Numbers")
plt.ylabel("Square of Prime Numbers")
plt.title("Prime Numbers vs Square ")


x=np.array(composite_numbers)
y=np.array(square_root_composite_numbers)
plt.subplot(1, 2, 2)
plt.scatter(x,y)
plt.xlabel("Composite Numbers")
plt.ylabel("Square root of Composite Numbers")
plt.title("Composite Numbers vs Square root")
# set the spacing between subplots
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()
